import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.signal import savgol_filter

def plot_wl(mygram):
    sns.set(color_codes=True)
    word_len = mygram.wl_df['avg_chars']
    wl = word_len[word_len.index[117:]] #slicing
    max_wl = wl.max()
    theyear = wl[wl == max_wl].index[0]
    # Smoothing
    new_wl = pd.Series(savgol_filter(wl, 39, 2), index=range(1701, 2009))
    wl.plot(linewidth=0.5,color="grey")
    new_wl.plot(linewidth=3, figsize=(15,8))
    plt.xlabel('Year', fontsize=16)
    plt.ylabel('Average Word Length', fontsize=16)
    plt.title('Word Length History 1700 - 2008', fontsize=18)
    plt.annotate('max: ' + str(max_wl)[:5] + '\nyear: ' + str(theyear), xy=(theyear, max_wl), xytext=(1970, 6.6), arrowprops=dict(facecolor='black', shrink=0.05, width=1))
