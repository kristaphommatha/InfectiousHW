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


def plot_violin_data(data, column_names_array, colors, ylabel, fig_title):
    fig, ax = plt.subplots()
    violins = ax.violinplot(data,showmeans=True)
    for i, violin in enumerate(violins['bodies']):
        violin.set_facecolor(colors[i])
    for partname in ('cbars', 'cmins', 'cmaxes', 'cmeans'):
        vp = violins[partname]
        vp.set_edgecolor(colors)
    ax.set_xticks([1,2,3])
    ax.set_xticklabels(column_names_array)
    ax.set_ylabel(ylabel)
    ax.spines[['right', 'top']].set_visible(False)
    plt.savefig(fig_title)


def plot_points_data(data, column_names_array, colors, ylabel, fig_title, cutoff=-1):
    fig, ax = plt.subplots()
    counter = 0
    for col in column_names_array:
        ax.scatter(np.random.normal(counter+1,0.1,len(data[col])),data[col],color=colors[counter],alpha=0.2)
        counter = counter + 1
    if cutoff != -1:
        ax.axhline(y=cutoff,linestyle='--',color='black')
    ax.set_xticks([1,2,3])
    ax.set_xticklabels(column_names_array)
    ax.set_ylabel(ylabel)
    ax.spines[['right', 'top']].set_visible(False)
    plt.savefig(fig_title,dpi=300)


def calc_se(c, data):
    pos_count = 0
    for case in data['Positive Ctrl']:
        if case >= c:
            pos_count = pos_count + 1
    se = pos_count/len(data['Positive Ctrl'])
    return se


def calc_sp(c, data):
    neg_count = 0
    for case in data['Negative Ctrl']:
        if case < c:
            neg_count = neg_count + 1
    sp = neg_count/len(data['Negative Ctrl'])
    return sp


def calc_raw_prev(c, data):
    se = calc_se(c,data)
    sp = calc_sp(c,data)

    pos_count = 0
    for case in data['Data']:
        if case >= c:
            pos_count = pos_count + 1
    raw_prev = pos_count/len(data['Data'])
    return raw_prev


def calc_corr_prev(c, data):
    se = calc_se(c,data)
    sp = calc_sp(c,data)
    raw_prev = calc_raw_prev(c, data)
    corr_prev = (raw_prev-(1-sp))/(se+sp-1)
    return corr_prev


def calc_Jc(c, data):
    se = calc_se(c,data)
    sp = calc_sp(c,data)
    Jc = se + sp - 1
    return Jc


def find_Youden(data, step):
    Jc_list = []
    c_list = np.arange(data['Negative Ctrl'].min(), data['Positive Ctrl'].max() + step, step)  # create list of c's to iterate thru
    for c in c_list:
        Jc = calc_Jc(c,data)
        Jc_list.append((c, Jc))
    max_index = max(enumerate(Jc_list), key=lambda x: x[1][1])[0]
    max_c = Jc_list[max_index][0]

    return(max_c)


def main():
    files_array = ['data/HW4_Q3_neg.csv','data/HW4_Q3_pos.csv','data/HW4_Q3_data.csv']
    column_names_array = ['Negative Ctrl', 'Positive Ctrl', 'Data']
    colors = ['red','black','blue']

    data = load_data(files_array, column_names_array, 'data/Q3data.xlsx')
    
    step = 0.1
    c = find_Youden(data, step)
    
    plot_points_data(data, column_names_array, colors, 'Prevalence', 'figs/Q3.png', cutoff=c)
    print(f'Youden Cutoff = {c}')


if __name__ == '__main__':
    main()
