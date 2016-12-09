import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_count_vs_rank(mygram):
    sns.set(color_codes=True)
    fig, axs = plt.subplots(2,2)
    mygram.word_rank(1850).plot(ax=axs[0][0], loglog=True, figsize=(8,6), legend=False, title='1850').set_ylabel('count')
    mygram.word_rank(1900).plot(ax=axs[0][1], loglog=True, figsize=(8,6), legend=False, title='1900').set_ylabel('count')
    mygram.word_rank(1950).plot(ax=axs[1][0], loglog=True, figsize=(8,6), legend=False, title='1950').set_ylabel('count')
    mygram.word_rank(2000).plot(ax=axs[1][1], loglog=True, figsize=(8,6), legend=False, title='2000').set_ylabel('count')
    plt.tight_layout()
    plt.suptitle('Word count vs. its rank on log log plots', fontsize=16, y=1.05)
