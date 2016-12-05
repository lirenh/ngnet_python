class NGram:
    """
    Stores all the 1-grams data, with some functions computing the data needed to draw diagrams.
    """
    def __init__(self, words_file, counts_file):
        df0 = pd.read_csv(words_file, header=None, names=['word','year','count','sources'], delim_whitespace=True)
        # alltime history Dataframe
        self.counts_df = pd.read_csv(counts_file, header=None, names=['year','total_words','pages','sources'], index_col=0)
        # use word as the index to speedup queries
        df1 = df0.set_index('word')
        merged = pd.merge(df1, self.counts_df, how='left', left_on='year', right_index=True) # TODO sort=False
        # save weight (relative frequency) in self.df
        merged['weight'] = merged['sources_x']/merged['total_words']
        self.df = merged[['year','count', 'sources_x', 'weight']].fillna(0)
        self.df.columns = ['year','count', 'sources', 'weight']
        # lazy
        self.wl_cached = False

    def count_in(self, word, year):
        """
        Returns the absolute count of WORD in YEAR. Returns 0 if the word did not appear in that year.
        """
        try:
            return self.df[self.df['year'] == year].at[word, 'count']  # TODO df.loc['quantity'] index first
        except KeyError:
            return 0

    def count_during(self, word, start, end):
        pass

    def alltime_history(self):
        """
        Returns a Dataframe recording the total number of 1-grams contained in the books.
        index: year  columns: total_words, pages, sources
        """
        return self.counts_df

    def word_history(self, word, start, end):
        """
        Returns a Dataframe contains history of the given WORD.
        index: word, columns: year (START to END), count, sources, weight
        """
        try:
            hist = self.df.loc[word]
            criterion = hist['year'].map(lambda x: x>=start and x<=end)
            return hist[criterion]
        except KeyError:
            print("cannot find the word!")

    def weight_history(self, word, start, end):
        pass

    def hist_sum(self, words, start, end):
        """
        Returns a Dataframe contains sum of history of the given words.
        index: year, columns: count, weight
        """
        result = pd.DataFrame()
        for word in words:
            # if the word doesn't exist, ignore it rather than throwing an exception
            if word not in self.df.index:
                continue
            # use year as the index
            result = self.df[['year', 'count', 'weight']].loc[word].set_index('year').add(result, fill_value=0)
        return result

    @property
    def wl_df(self):
        """
        Returns a Dataframe contains average word length history.
        index: year  columns: count, chars, avg_chars
        """
        if self.wl_cached == True:
            return self.__avgdf
        else:
            df0['chars'] = df0['word'].map(lambda x: len(x)) * df0['count']
            self.__avgdf = df0[['year', 'count', 'chars']].groupby('year').sum()
            self.__avgdf['avg_chars'] = self.__avgdf['chars'] / self.__avgdf['count']
            self.wl_cached = True
            return self.__avgdf
