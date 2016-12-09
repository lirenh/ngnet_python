#!/bin/bash

for i in http://storage.googleapis.com/books/ngrams/books/googlebooks-eng-all-1gram-20120701-{a..z}.gz
do wget -P data/ngrams/ "$i"
done

for j in data/ngrams/googlebooks-eng-all-1gram-20120701-{a..z}.gz
do gzip -d "$j"
done

wget -P data/ngrams/ http://storage.googleapis.com/books/ngrams/books/googlebooks-eng-all-totalcounts-20120701.txt
