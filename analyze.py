"""
analyze.py - Are song lyrics getting simpler? (Billboard Hot 100, 1965-2015)
============================================================================
For each year-end hit we measure four things and watch how they drift over 50 years:

  * length            - words per song
  * lexical diversity - unique words among the first 100 words (length-controlled)
  * repetition        - zlib compression ratio (more repetitive -> compresses smaller)
  * word length       - average characters per word

Lyrics here are lowercased with punctuation stripped, so we deliberately avoid
sentence-based readability and stick to robust vocabulary measures.

Outputs: figures/*.png and tables/by_year.csv
"""
import os
import zlib
import numpy as np
import pandas as pd
from scipy import stats
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(__file__)
FIG = os.path.join(HERE, "figures"); TAB = os.path.join(HERE, "tables")
INK, GOLD, TEAL, CORAL, PLUM = "#1a1a2e", "#D4A537", "#15868C", "#E0567A", "#5B4B8A"
plt.rcParams.update({"figure.dpi": 200, "savefig.dpi": 200, "font.size": 12,
    "axes.edgecolor": "#888", "axes.grid": True, "grid.color": "#e8e2d4",
    "axes.axisbelow": True, "figure.facecolor": "white", "axes.facecolor": "white"})


def song_metrics(lyrics):
    toks = str(lyrics).split()
    n = len(toks)
    if n < 50:
        return None
    ttr100 = len(set(toks[:100])) / 100 if n >= 100 else len(set(toks)) / n
    raw = (" ".join(toks)).encode("utf-8")
    comp = len(zlib.compress(raw, 6)) / len(raw)
    avg_len = np.mean([len(t) for t in toks])
    return dict(words=n, lex_div=ttr100, compress=comp, word_len=avg_len)


def load():
    df = pd.read_csv(os.path.join(HERE, "data", "billboard_lyrics_1964-2015.csv"),
                     encoding="latin-1")
    df = df.dropna(subset=["Lyrics", "Year"])
    df["Year"] = pd.to_numeric(df["Year"], errors="coerce")
    df = df[(df["Year"] >= 1965) & (df["Year"] <= 2015)]
    recs = []
    for _, r in df.iterrows():
        m = song_metrics(r["Lyrics"])
        if m:
            m["Year"] = int(r["Year"]); recs.append(m)
    return pd.DataFrame(recs)


def trend(ax, by, col, color, title, ylab):
    ax.plot(by["Year"], by[col], "-o", color=color, lw=2, ms=4, alpha=0.85)
    sl, ic, r, p, _ = stats.linregress(by["Year"], by[col])
    xs = np.array([by["Year"].min(), by["Year"].max()])
    ax.plot(xs, ic + sl*xs, color=INK, ls="--", lw=1.8, label=f"trend (r={r:.2f})")
    ax.set_title(title, color=INK, weight="bold"); ax.set_ylabel(ylab); ax.set_xlabel("Year")
    ax.legend(fontsize=9)
    return sl, r, p


def main():
    os.makedirs(FIG, exist_ok=True); os.makedirs(TAB, exist_ok=True)
    df = load()
    by = df.groupby("Year").mean(numeric_only=True).reset_index()
    by["n"] = df.groupby("Year").size().values
    by.to_csv(os.path.join(TAB, "by_year.csv"), index=False)
    print(f"Songs analyzed: {len(df):,} across {by['Year'].nunique()} years\n")

    metrics = [
        ("words",    "01_length",      TEAL, "Hit songs have gotten much longer",          "Words per song"),
        ("lex_div",  "02_diversity",   PLUM, "Vocabulary in the first 100 words held steady", "Unique words per 100 words"),
        ("compress", "03_repetition",  CORAL,"Whole songs repeat more (and are longer)",   "Compression ratio (lower = more repetitive)"),
        ("word_len", "04_word_length", GOLD, "Words stayed about the same length",          "Avg. characters per word"),
    ]
    rows = []
    for col, fname, color, title, ylab in metrics:
        fig, ax = plt.subplots(figsize=(8.2, 4.6))
        sl, r, p = trend(ax, by, col, color, title, ylab)
        fig.tight_layout(); fig.savefig(f"{FIG}/{fname}.png"); plt.close(fig)
        d_early = by[by.Year <= 1969][col].mean()
        d_late = by[by.Year >= 2010][col].mean()
        rows.append({"metric": col, "1965-69_avg": round(d_early, 3), "2010-15_avg": round(d_late, 3),
                     "pct_change": round((d_late/d_early-1)*100, 1), "slope_per_yr": round(sl, 4),
                     "r_vs_year": round(r, 2), "p": round(p, 4)})
        print(f"  {col:9} {d_early:7.2f} -> {d_late:7.2f}  ({(d_late/d_early-1)*100:+5.1f}%)  r={r:+.2f} p={p:.3f}")

    pd.DataFrame(rows).to_csv(os.path.join(TAB, "trends.csv"), index=False)
    print("\nSaved figures + tables/")


if __name__ == "__main__":
    main()
