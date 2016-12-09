import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_hypnoyms(mynet, mygram):
    sns.set(color_codes=True)
    inc_set = mynet.hypnoyms('increase')
    dec_set = mynet.hypnoyms('decrease')
    inc_dict, dec_dict = {}, {}
    for inc in inc_set:
        count = mygram.count_in(inc, 1900)
        if count == 0:
            continue
        inc_dict[inc] = count
    for dec in dec_set:
        count = mygram.count_in(dec, 1900)
        if count == 0:
            continue
        dec_dict[dec] = count
    inc_s = pd.Series(inc_dict, name=' ')
    dec_s = pd.Series(dec_dict, name=' ')
    fig, axs = plt.subplots(2,1)
    inc_s.sort_values(axis=0, ascending=False).head(15).plot.pie(autopct='%.2f', ax=axs[0], legend=False, title="increase\'s top 15 hyponyms in 1900", figsize=(8,10))
    dec_s.sort_values(axis=0, ascending=False).head(15).plot.pie(autopct='%.2f', ax=axs[1], legend=False, title="decrease\'s top 15 hyponyms in 1900", figsize=(8,10))
