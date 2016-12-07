import pandas as pd

class NGram:
    def __init__(self, words_file, counts_file):
        #self.df0 = pd.read_csv(words_file, header=None, names=['word','year','count','sources'], delim_whitespace=True)
        self.df0 = pd.read_csv(words_file)
        # alltime history Dataframe
        self.counts_df = pd.read_csv(counts_file, header=None, names=['year','total_words','pages','sources'], index_col=0)
        # use word as the index to speedup queries
        df1 = self.df0.set_index('word')
        merged = pd.merge(df1, self.counts_df, how='left', left_on='year', right_index=True) # TODO sort=False
        # save weight (relative frequency) in self.df
        merged['weight'] = merged['count']/merged['total_words']
        self.df = merged[['year','count', 'sources_x', 'weight']].fillna(0)
        self.df.columns = ['year','count', 'sources', 'weight']
        # lazy
        self.wl_cached = False
        self.rank_cached = False

    def count_in(self, word, year):
        """
        Returns the absolute count of WORD in YEAR. Returns 0 if the word did not appear in that year.
        """
        try:
            return self.df[self.df['year'] == year].at[word, 'count']  # TODO df.loc['quantity'] index first
        except KeyError:
            return 0

    def alltime_history(self):
        """
        Returns the yearly record of the total number of 1-grams in a Dataframe.
        index: year  columns: total_words, pages, sources
        """
        return self.counts_df

    def word_history(self, word, start, end):
        """
        Returns thehistory of the given WORD in a Dataframe. Throws KeyError if not found.
        index: year, columns: count, sources, weight
        """
        hist = self.df.loc[word]
        criterion = hist['year'].map(lambda x: x>=start and x<=end)
        return hist[criterion].set_index('year')

    def hist_sum(self, words, start, end):
        """
        Returns the sum of history of the given words in a Dataframe.
        index: year, columns: count, weight
        """
        result = pd.DataFrame()
        for word in words:
            # if the word doesn't exist, ignore it rather than throwing an exception
            if word not in self.df.index:
                continue
            # use year as the index
            result = self.df[['year', 'count', 'weight']].loc[word].set_index('year').add(result, fill_value=0)
        criterion = result.index.map(lambda x: x>=start and x<=end)  # TODO apply boolean indexing before addition
        return result[criterion]

    @property
    def wl_df(self):
        """
        Returns the average word length history in a Dataframe.
        index: year  columns: count, chars, avg_chars
        """
        if self.wl_cached == True:
            return self.__avgdf
        else:
            self.df0['chars'] = self.df0['word'].map(lambda x: len(str(x))) * self.df0['count']
            self.__avgdf = self.df0[['year', 'count', 'chars']].groupby('year').sum()
            self.__avgdf['avg_chars'] = self.__avgdf['chars'] / self.__avgdf['count']
            self.wl_cached = True
            return self.__avgdf

    def word_rank(self, year):
        """
        Returns word rankings of the given year in a Dataframe.
        index: rank column: count
        """
        yearly_record = self.df0[self.df0['year'] == year]
        words_total_count = yearly_record[['word','count']].groupby('word', sort=False).sum()  # sort=True?
        words_sorted = words_total_count.sort_values(by="count", ascending=False)
        words_sorted['rank'] = range(1, len(words_sorted.index) + 1, 1)
        return words_sorted.set_index('rank')
