import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_comparison(mygram, word_lst):
    sns.set(color_codes=True)
    hists = []
    for w in word_lst:
        hists.append(mygram.word_history(w, 1850, 2008))

    hsum = pd.DataFrame()
    for df in hists:
        hsum = hsum.add(df, fill_value=0)

    max_combined_weight = hsum['weight'].max()
    max_year = hsum[hsum['weight'] == max_combined_weight].index[0]

    plt.figure(figsize=(15, 8))
    color = ['r', 'b', 'c', 'm', 'k', 'w']
    for i in range(len(word_lst)):
        sns.tsplot(hists[i]['weight'], time=hists[i].index, condition=word_lst[i], value='weight', color=color[i])
    plt.axvline(x=max_year, linewidth=1, color='g')
    plt.text(1965, 2.2E-5, 'max combined\nweight in ' + str(max_year))
    plt.xlabel('Year', fontsize=16)
    plt.ylabel('Weight (Relative Frequency)', fontsize=16)
    plt.title('Ideology: socialism vs. capitalism 1850 - 2008', fontsize=18)
