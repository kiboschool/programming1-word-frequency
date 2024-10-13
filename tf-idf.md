# Bonus task: Implementing TF-IDF

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

Implementing TF-IDF is a challenging task. Only start it if you are feeling
ahead of the rest of your work.

## Steps

The overall search system will take in a _search term_ and a _list of
documents_, and return the documents ranked in order of their TF-IDF score.

1. Start by implementing a `term_frequency` function by using your `word_frequency`
function. `term_frequency` is the _relative frequency_ of the term within the
document: the number of times it appears, divided by the total number of words
in the document.

$$
tf(term, document) = count(term, document) / word\_count(document)
$$

2. Next, implement `inverse_document_frequency`. Inverse Document Frequency is
defined as logarithm of the total number of documents divided by the number of
documents that contain the term.

$$
idf(term, documents) = log( \frac{len(documents)}{count\_containing(term, documents)} )
$$

3. Now, you can implement a `tf_idf` function, which is the term frequency times the inverse document frequency:

$$
tf\_idf(term, document, documents) = tf(term, document) * idf(term, documents)
$$

4. Finally, you can write a `search` function, which takes in a search term and prints out the document with the highest `tf_idf` score.

## Notes

There are lots of ways to write this code, and different features you might want to use to make it more effective and performant.

For instance, if you recompute the idf for each term for every document, you end up doing the same work again lots of times. Instead, you could try to write the code so that the idf is only computed once for the document.

Similarly - if you store the word frequencies (or term frequencies) for each of the documents, you can use those word frequencies instead of re-computing them each time.

You could make your search function work for a fixed set of documents, or allow the user to pass in a list of documents to search. There are lots of possibilities to explore. Share your solution and observations with the community in Discord if you are interested!