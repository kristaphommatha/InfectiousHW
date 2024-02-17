import sys
sys.path.insert(0, '../HW1')
import HW1Q1 as HW1Q1
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import math


def get_sis_model(s0, i0, beta, gamma, t_frame, delta_t):
    s = [s0]
    i = [i0]
    curr_s = s0
    curr_i = i0
    t = 0

    while t <= t_frame:
        dsdt = -beta * curr_s * curr_i + gamma * curr_i
        didt = beta * curr_s * curr_i - gamma * curr_i

        curr_s = HW1Q1.forward_euler(curr_s, delta_t, dsdt)
        curr_i = HW1Q1.forward_euler(curr_i, delta_t, didt)

        s.append(curr_s)
        i.append(curr_i)
        t = t + delta_t

    return s, i


def get_analytical_i(i0, beta, gamma, t_frame, delta_t):
    R0 = beta/gamma
    i = [i0]
    t = 0
    while t <= t_frame:
        new_i = (1 - 1/R0)/(1+(1-1/R0-i0)/i0 * math.exp(-(beta-gamma)*t))
        i.append(new_i)
        t = t + delta_t

    return i


def plot_Q1a(e_i, a_i, beta, gamma, t_frame, delta_t, fig_title):
    t = 0
    t_plot = [t]
    while t <= t_frame:
        t_plot.append(t)
        t = t + delta_t

    fig, ax = plt.subplots()
    ax.plot(t_plot,e_i,label='Forward Euler',color='red')
    ax.plot(t_plot,a_i,label='Analytical',color='black',linestyle='--')
    ax.set_xlabel('Time')
    ax.set_ylabel('i(t)')
    ax.set_ylim(0,0.5)
    ax.set_title(f'Normalized SIS Model, delta_t = {delta_t}')
    ax.legend(loc='lower right')
    plt.savefig(fig_title,dpi=100)


def main():
    beta = 3
    gamma = 2
    s0 = 0.99
    i0 = 1 - s0
    t_frame = 25
    delta_ts = [2, 1, 0.5]

    for delta_t in delta_ts:
        e_s = []
        e_i = []
        a_i = []
        e_s, e_i = get_sis_model(s0, i0, beta, gamma, t_frame, delta_t)
        a_i = get_analytical_i(i0, beta, gamma, t_frame, delta_t)

        plot_Q1a(e_i, a_i, beta, gamma, t_frame, delta_t, f'Q1_dt{delta_t}.png')


if __name__ == '__main__':
    main()
