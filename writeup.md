# Are song lyrics getting simpler? Billboard Hot 100, 1965–2015

Hit songs from 2010–15 are about twice as long as hits from the late 1960s, and as whole documents they repeat more. Their vocabulary did not shrink, though, and the words in them are the same length they were in 1965. That is the short answer to the claim that pop lyrics have been getting simpler and more repetitive, which is what I set out to test.

## Data and measures

The lyrics are the Billboard Year-End Hot 100 from 1965 to 2015 in the `walkerkq/musiclyrics` dataset: 4,816 songs once anything under 50 words is dropped. They come lowercased with the punctuation stripped, so there are no sentences to feed a readability score. I scored each song four ways and averaged the scores by year:

- words per song;
- unique words among the first 100 (lexical diversity, controlled for length);
- zlib compression ratio, where lower means more repetitive;
- mean word length in characters.

## Results

Comparing the 1965–69 average with the 2010–15 average (from `tables/trends.csv`):

- Words per song went from 200 to 413, +107%, r = 0.92.
- The compression ratio fell from 0.357 to 0.290, −19%, r = −0.89, so whole songs repeat more.
- Unique words in the first 100 rose slightly, from 57.5 to 61.4, +7%, r = 0.58.
- Characters per word went from 3.84 to 3.83, −0.3%. The slope is statistically detectable (r = −0.46), but it amounts to one hundredth of a character.

"Simpler" is the wrong word for this. Hits got much longer and lean harder on repeated hooks, which listeners hear as repetition; the vocabulary is at least as varied as before and the words are no shorter. One caution on the repetition result: compression is partly a length artifact, because a longer song gives the compressor more material to match against. The length-controlled diversity measure is there as the check on that.

## Limitations

The Year-End chart is a sales ranking, so any change in its genre mix moves every one of these measures, and the analysis does not split results by genre. Each yearly mean rests on 86 to 100 songs.

Code: `analyze.py`. Figures: `figures/`.
