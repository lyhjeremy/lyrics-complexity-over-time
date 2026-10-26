# Are song lyrics getting simpler? Billboard Hot 100, 1965–2015

**Question.** Have hit-song lyrics become simpler and more repetitive?

**Data.** Billboard Year-End Hot 100 lyrics from 1965 to 2015 (`walkerkq/musiclyrics`), 4,816 songs with at least 50 words. The lyrics are lowercased with punctuation stripped, which rules out sentence-based readability scores.

**Measures.** Each song gets four scores, then songs are averaged by year: words per song; unique words among the first 100 words (lexical diversity controlled for length); zlib compression ratio (lower means more repetitive); and mean word length in characters.

**Results** (1965–69 average against 2010–15 average, from `tables/trends.csv`):

- Words per song: 200 to 413, +107%, r = 0.92.
- Compression ratio: 0.357 to 0.290, −19%, r = −0.89. Whole songs repeat more.
- Unique words in the first 100: 57.5 to 61.4, +7%, r = 0.58. Slightly up.
- Characters per word: 3.84 to 3.83, −0.3%. The slope is statistically detectable (r = −0.46) but amounts to one hundredth of a character.

**Interpretation.** "Simpler" is the wrong word. Hits are much longer and lean harder on repeated hooks, which listeners hear as repetition, but the vocabulary is no less varied and the words are no shorter. The compression measure is partly a length artifact, since longer songs give the compressor more to match. The length-controlled diversity measure is the check on that.

**Limitations.** The chart is a sales ranking, so changes in genre mix move every measure, and the analysis does not split by genre. Each yearly mean rests on 86 to 100 songs.

Code: `analyze.py`. Figures: `figures/`.
