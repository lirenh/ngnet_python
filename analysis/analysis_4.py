import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def boxplot_hyponyms(mynet, mygram, word_lst):
    sns.set(color_codes=True)
    hyponyms_lst, series_lst = [], []
    for w in word_lst:
        hyponyms_lst.append(mynet.hyponyms(w))

    def iter(theset):
        f_dict = {}
        for f in theset:
            count = mygram.count_in(f, 2000)
            if count == 0:
                continue
            f_dict[f] = count
        return f_dict

    for i in range(len(word_lst)):
        f_s  = pd.Series(iter(hyponyms_lst[i]), name = word_lst[i])
        sorted = f_s.sort_values(axis=0, ascending=False).head(20)
        series_lst.append(sorted.reset_index()[word_lst[i]])

    words_df = pd.concat(series_lst, axis=1)
    plt.figure(figsize=(8, 6))
    ax = sns.boxplot(data=words_df)
    ax = sns.swarmplot(data=words_df, color=".25")
    plt.ylabel("count")
    plt.title("Comparison of 4 classical elements' hyponyms in 2000", fontsize=16, y=1.05)
