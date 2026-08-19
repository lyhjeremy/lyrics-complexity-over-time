# Are Song Lyrics Getting Simpler?

Design and copy follow [these standards](https://github.com/lyhjeremy/lyhjeremy/blob/main/DESIGN_STANDARDS.md).

Fifty years of Billboard Year-End Hot 100 hits (1965–2015), analyzed. The popular
claim is that lyrics got "dumber and more repetitive." The data says it's more
nuanced: hit songs **more than doubled in length** and got **more repetitive
overall**, but the words themselves are **no shorter or less varied**.

> **Read the story:** https://lyhjeremy.github.io/lyrics-complexity-over-time/
> **In depth:** https://lyhjeremy.github.io/lyrics-complexity-over-time/overview/

## Findings (4,816 songs)
- **Length +107%** (≈200 → ≈410 words/song; r = 0.92).
- **Whole-song repetition up** (compression ratio r = −0.89). Partly a length effect.
- **Vocabulary richness steady** (unique words per 100 words even rose ~7%).
- **Word length flat** (no change across 50 years).

## Reproduce
```bash
pip install -r requirements.txt
python fetch_data.py     # downloads the Billboard lyrics dataset to data/
python analyze.py        # writes figures/ and tables/
```

## Data & method
Billboard Year-End Hot 100 lyrics 1965–2015 (public dataset
[walkerkq/musiclyrics](https://github.com/walkerkq/musiclyrics)), songs with ≥50
words. Lyrics are lowercased with punctuation stripped, so the analysis uses
length-robust vocabulary measures (words/song, unique words in a fixed 100-word
window, zlib compression ratio for repetition, mean word length) rather than
sentence-based readability. Raw data is downloaded by `fetch_data.py` and git-ignored.

## License
[MIT](LICENSE) © 2026 Jeremy Lee
