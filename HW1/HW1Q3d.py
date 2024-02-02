import HW1Q1 as Q1
import HW1Q3 as Q3
import numpy as np
from scipy.optimize import fsolve
import matplotlib
matplotlib.use('Agg')  # noqa
import matplotlib.pyplot as plt


def plot_SIR_r_inf(S, I, R, N, t_frame, beta, gamma, r_inf, fig_title):
    t_plot = list(range(0, t_frame + 1, 1))
    r_plot = [r_inf for t in t_plot]
    s = [S_val/N for S_val in S]
    i = [I_val/N for I_val in I]
    r = [R_val/N for R_val in R]

    fig, ax = plt.subplots()
    ax.plot(t_plot,s,label='r Krista')
    ax.plot(t_plot,i,label='i Krista')
    ax.plot(t_plot,r,label='r Krista')
    ax.plot(t_plot,r_plot,label='r_infinity',color='green',linestyle='dashed')
    ax.set_xlabel('Time')
    ax.set_ylabel('Population Fraction')
    ax.set_title(f'Q3d. SIR Model (beta = {beta}, gamma = {gamma})')
    ax.legend(loc='lower right')
    plt.savefig(fig_title,dpi=100)


def main():
    S0 = 999
    I0 = 1
    N = 1000
    t_frame = 50
    beta = 1
    gamma = 0.5
    R0 = [beta/gamma]

    solns = Q1.get_SIR_model(S0, I0, N, beta, gamma, t_frame)
    r_inf_arr = Q3.find_intersection(R0)
    r_inf = r_inf_arr[0][0]

    plot_SIR_r_inf(solns[0], solns[1], solns[2], N,
             t_frame, beta, gamma, r_inf,'Q3d_SIR.png')


if __name__ == '__main__':
    main()