import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import Q1a


def main():
    data = Q1a.I_from_incidence('data/all_weeks.csv')
    last_points = data.iloc[-100:]
    i_eq = last_points["I(t)"].mean()
    err = last_points["I(t)"].std()
    m,b = Q1a.plot_lin_reg(last_points,'Week','I(t)','figs/Q1_EQMPeriod',linReg=True)
    print(f'Slope = {m}, Intercept = {b}')
    print(f'Average = {i_eq}, Std Dev = {err}')


if __name__ == '__main__':
    main()