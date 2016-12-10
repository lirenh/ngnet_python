# NGrams and WordNet
<div id="table-of-contents">
<h2>Table of Contents</h2>
<div id="text-table-of-contents">
<ul>
<li><a href="#sec-1">1. Project structure</a></li>
<li><a href="#sec-2">2. Raw Data</a></li>
<li><a href="#sec-3">3. Analyses</a>
<ul>
<li><a href="#sec-3-1">3.1. Average word length history</a></li>
<li><a href="#sec-3-2">3.2. socialism vs. capitalism</a></li>
<li><a href="#sec-3-3">3.3. Hyponyms of increase vs. decrease</a></li>
<li><a href="#sec-3-4">3.4. Zipf's Law</a></li>
<li><a href="#sec-3-5">3.5. Four classical elements</a></li>
</ul>
</li>
</ul>
</div>
</div>


# Project structure<a id="sec-1" name="sec-1"></a>

    ├── analysis/
    │   ├── analysis_1.py  # average word length history
    │   ├── analysis_2.py  # socialism vs. capitalism
    │   ├── analysis_3.py  # hyponyms of increase vs. decrease
    │   ├── analysis_4.py  # four classical elements pie chart
    │   └── analysis_5.py  # zipf's law
    │
    ├── analysis_results.ipynb
    ├── collect_data.sh
    ├── processing_data.py # process raw data and save it to output/
    ├── config.py  # stores data paths
    │
    ├── ngnet/
    │   ├── digraph.py  # used to organize synsets relationships
    │   ├── ngram.py    # a class storing Google NGram data. It's used in various analyses to access the required data fast
    │   └── wordnet.py  # a class storing WordNet data. It's mainly used to get hyponyms of a given word
    │
    ├── output/  # all data pushed to github is dummy data with only 10k entries
    │   ├── dummy-mini_ngrams.csv  # minimal ngram
    │   ├── ngrams_lower_alpha/    # lowercase alphabetic nouns
    │   ├── ngrams_noun/           # nouns
    │   ├── pics/
    │   ├── total_counts.csv
    │   └── wordnet/
    │
    ├── raw_data/
    │   ├── ngrams/
    │   └── wordnet/
    │
    └── tests/

# Raw Data<a id="sec-2" name="sec-2"></a>

-   `googlebooks-eng-all-1gram-20120701-*.csv`

Tab-separated ngrams data. Example below: In 1978, the word "circumvallate", occurred 335 times overall, in 91 distinct books.  

    circumvallate   1978   335    91

-   `total_counts.csv`

Records the total number of 1-grams contained in the books. Example below: In 1505, the number of total words recorded is 32059, from 231 pages, 1 book.:

    1505,32059,231,1

-   `synsets.csv`

Lists of all the noun synsets in WordNets. The first field is the synset id (an integer), the second field is the synset, and the third field is its definition:

    36,AND_circuit AND_gate,a circuit in a computer that fires only when all of its inputs fire

-   `hyponyms.csv`

Contains the hyponym relationships: The first field is a synset id; subsequent fields are the ids of the synset's direct hyponyms:

    79537,38611,9007

# Analyses<a id="sec-3" name="sec-3"></a>

## Average word length history<a id="sec-3-1" name="sec-3-1"></a>

![analysis1](./output/pics/word_length.png)  
**Observation:**  
The average word length was slowly increasing across the history and reached its peak at 6.947 chars/word in 1979.  

## socialism vs. capitalism<a id="sec-3-2" name="sec-3-2"></a>

![analysis2](./output/pics/ideology.png)  
**Observation:**  
The two ideology were mentioned most around 1940 and 1980. They are losing momentum quickly in recent years.  

## Hyponyms of increase vs. decrease<a id="sec-3-3" name="sec-3-3"></a>

![analysis3](./output/pics/hyponyms_pie.png)  
**Observation:**  
People didn't tend to use "decrease" to express its meanings. It wasn't even among the top 15 of its own hyponyms.  

## Zipf's Law<a id="sec-3-4" name="sec-3-4"></a>

![analysis4](./output/pics/zipfs.png)  
**Observation:**  
All loglog plots show a straight line, which means the frequency of words is proportional to the rank. It's an interesting fact since the ranking of a word shouldn't have any numerical properties.  

## Four classical elements<a id="sec-3-5" name="sec-3-5"></a>

![analysis5](./output/pics/hyponyms_box.png)  
**Observation:**  
Many words have related meanings with the 4 classical elements. In 2000 their "strength" is in the order of air > earth > water > fire. Words relating to "fire" is barely used.
