import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def load_data(files_array, column_names_array, filename):
    data = pd.DataFrame()
    for f,n in zip(files_array,column_names_array):
        file_data = pd.read_csv(f,header=None)
        data[n] = file_data[0]
    data.to_excel(filename, index=False)
    return data


def plot_data(data, column_names_array, fig_title):
    fig, ax = plt.subplots()
    violins = ax.violinplot(data,showmeans=True)
    colors = ['red','black','blue']
    for i, violin in enumerate(violins['bodies']):
        violin.set_facecolor(colors[i])
    for partname in ('cbars', 'cmins', 'cmaxes', 'cmeans'):
        vp = violins[partname]
        vp.set_edgecolor(colors)
    ax.set_xticks([1,2,3])
    ax.set_xticklabels(column_names_array)
    ax.set_ylabel('Seroprevalance')
    ax.spines[['right', 'top']].set_visible(False)
    plt.savefig(fig_title)


def main():
    files_array = ['data/HW4_Q3_neg.csv','data/HW4_Q3_pos.csv','data/HW4_Q3_data.csv']
    column_names_array = ['Negative Ctrl', 'Positive Ctrl', 'Data']

    data = load_data(files_array, column_names_array, 'data/Q3data.xlsx')
    plot_data(data, column_names_array, 'figs/Q3.png')


if __name__ == '__main__':
    main()
