# Are song lyrics getting simpler? Billboard Hot 100, 1965-2015

**Question.** Have hit-song lyrics become simpler and more repetitive?

**Data.** Billboard Year-End Hot 100 lyrics 1965-2015 (`walkerkq/musiclyrics`),
4,816 songs with at least 50 words. Lyrics are lowercased, punctuation stripped.

**Measures (per song, averaged by year).** words per song; unique words among the
first 100 words (length-controlled lexical diversity); zlib compression ratio
(lower = more repetitive); mean word length.

**Results.**
- Words per song: ~200 (1965-69) -> ~413 (2010-15), +107%, r = 0.92.
- Compression ratio: 0.36 -> 0.29, -19%, r = -0.89 (more repetitive overall).
- Lexical diversity (first 100 words): 0.57 -> 0.61, +7%, r = 0.58 (steady/slightly up).
- Word length: ~3.84 -> ~3.83 chars, flat.

**Interpretation.** "Simpler" is the wrong word. Hits are much longer and lean
harder on repeated hooks (which listeners perceive as repetitive), but they are not
built from shorter or less-varied vocabulary. Note the compression measure is partly
a length artifact - longer songs repeat hooks by construction - which is why the
length-controlled diversity measure tells the complementary story.

See `analyze.py` and `figures/`.
