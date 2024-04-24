import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def I_from_incidence(data_file):
    data = pd.read_csv(data_file)
    incidence = data['New Cases']

    week_count = 1
    infections = []
    curr_incidence = 0
    prev_incidence = [0,0]  # first index is infections from the week before,
                            # second index is infections from two weeks before
    for i in incidence:
        if week_count == 1:
            infection_count = i
            infections.append(infection_count*10)
            prev_incidence[0] = i

        elif week_count == 2:
            infection_count = infection_count + i
            infections.append(infection_count*10)
            prev_incidence[1] = prev_incidence[0]
            prev_incidence[0] = i

        else:
            infection_count = infection_count + i - prev_incidence[1]
            infections.append(infection_count*10)
            prev_incidence[1] = prev_incidence[0]
            prev_incidence[0] = i

        week_count = week_count + 1

    data['I(t)'] = infections
    data.to_excel('data/Q1data.xlsx', index=False)
    return(data)


def get_exp_growth(data):
    start_index = 0
    end_index = data['I(t)'].idxmax()
    exp_growth = data.iloc[start_index:end_index]
    return exp_growth


def plot_lin_reg(data, x, y, out_file, order=1, linReg=True):
    fig, ax = plt.subplots()
    ax.scatter(data[x], data[y])
    if linReg is True:
        m, b = np.polyfit(data[x],data[y],order)
        ax.plot(data[x],m*data[x]+b,linestyle='--')
    ax.set_xlabel(x)
    ax.set_ylabel(y)
    ax.spines[['right', 'top']].set_visible(False)
    plt.savefig(out_file,dpi=300)
    if linReg is True:
        return m, b
    else:
        return np.nan


def main():
    data = I_from_incidence('data/all_weeks.csv')
    plot_lin_reg(data,'Week','I(t)','figs/Q1_IvsTime',linReg=False)
    exp_growth = get_exp_growth(data)
    plot_lin_reg(exp_growth,'Week','I(t)','figs/Q1_ExpGrowthPeriod',linReg=False)
    
    logI = []
    for i in exp_growth['I(t)']:
        logI.append(np.log(i))
    exp_growth['log(I(t))'] = logI
    m, b = plot_lin_reg(exp_growth,'Week','log(I(t))','figs/Q1_LinReg',linReg=True)
    print(f'Slope = {m}, Intercept = {b}')


if __name__ == '__main__':
    main()
