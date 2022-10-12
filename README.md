# Word Frequency

When analysing political speeches, analysts sometimes use _word frequency_ to
understand the themes of a speech or to compare how different politicians tend
to speak.

## Your Task

1. Write a function `word_frequency` that takes in a string of text and computes the
frequency of each word in the text. The return value should be a dictionary with
each different word as a key, and the number of times that word appears in the
text as the value.

2. Write a function `report_frequency` that takes in a string of text and calls
`word_frequency` to get the frequency of all the words in the text. It should
then print the top ten most used words and their frequencies.

## Starter Code

In `main.py` there is an empty function for `word_frequency` and
`report_frequency`, as well as a binding to run the `report_frequency` function
on a file if one is passed in like `python main.py file-to-check.txt`.

## Testing

Run the automated tests with `python test_main.py` to check your solution.

## Bonus: Normalization

If you run your word frequency program, you may have noticed that different
capitalizations of the same word end up counting as different words. Similarly,
if you split words by spaces, you may have words that include punctuation.

Write a new function `normalized_word_frequency` that fixes these errors. It
should lowercase each term and strip out any punctuation.

## Bonus: TF-IDF

A popular algorithm for ranking different documents in search engines is called
Term Frequency - Inverse Document Frequency.

Term Frequency says that if a search term occurs more often in a document, then
the document is more likely to be relevant. So, if `roses.txt` mentions the word
'flower' 10 times, then it is more relevant for the search term "flower", compared to a
`plants.txt` of the same length that only has the word 'flower' once.

By default, using Term Frequency to score documents would mean that a search
term like 'the' would make documents using 'the' very frequently rank
high in the search results. But, that word is really _common_. It's not giving
very much information about whether the document is relevant.

Inverse Document Frequency is a way to _reduce_ the score for terms that show up
commonly in different documents. It multiples the score by a factor depending on
how rare the term is across all the documents. A word like 'the' which appears
in every document will have almost no effect on the result ranking, but a less
commonly used word like 'flower' or a rare word like 'idempotent' would have a
strong impact on the ranking of the search results.

Word frequency plays a key role in computing TF-IDF scores. In a way, it's
at the heart of this core search engine algorithm.

If you're curious, you can try to implement a TF-IDF-based search ranking. See
tf-idf.md for more.