import sys
sys.path.insert(0, '../HW1')
import HW1Q1 as HW1Q1
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import math


def get_ANM(S0, I0, V0, N, VE, beta, gamma, t_frame, delta_t):
    S = [S0]
    I = [I0]
    Vo = [(1 - VE)*V0]
    R = [N - S0 - I0 - V0]
    curr_S = S0
    curr_I = I0
    curr_Vo = (1 - VE)*V0

    t = 0
    while t <= t_frame:
        dSdt = -beta * curr_S * curr_I / N
        dIdt = beta * curr_S * curr_I / N + beta * curr_Vo * curr_I / N - gamma * curr_I
        dVodt = - beta * curr_Vo * curr_I / N

        curr_S = HW1Q1.forward_euler(curr_S, delta_t, dSdt)
        curr_I = HW1Q1.forward_euler(curr_I, delta_t, dIdt)
        curr_Vo = HW1Q1.forward_euler(curr_Vo, delta_t, dVodt)

        S.append(curr_S)
        I.append(curr_I)
        Vo.append(curr_Vo)
        R.append(N - curr_S - curr_I - curr_Vo - VE*V0)

        t = t + delta_t

    return S, I, R


def get_leaky(S0, I0, V0, N, VE, beta, gamma, t_frame, delta_t):
    S = [S0]
    I = [I0]
    V = [V0]
    R = [N - S0 - I0 - V0]
    curr_S = S0
    curr_I = I0
    curr_V = V0

    t = 0
    while t <= t_frame:
        dSdt = -beta * curr_S * curr_I / N
        dIdt = beta * curr_S * curr_I / N + beta * curr_V * curr_I / N * (1 - VE) - gamma * curr_I
        dVdt = - beta * curr_V * curr_I / N * (1 - VE)

        curr_S = HW1Q1.forward_euler(curr_S, delta_t, dSdt)
        curr_I = HW1Q1.forward_euler(curr_I, delta_t, dIdt)
        curr_V = HW1Q1.forward_euler(curr_V, delta_t, dVdt)

        S.append(curr_S)
        I.append(curr_I)
        V.append(curr_V)
        R.append(N - curr_S - curr_I - curr_V)

        t = t + delta_t

    return S, I, R


def plot_vax_SIR(S, I, R, t_frame, delta_t, fig_title, file_name):
    t = 0
    t_plot = [t]
    while t <= t_frame:
        t_plot.append(t)
        t = t + delta_t

    fig, ax = plt.subplots()
    ax.plot(t_plot,S,label='S')
    ax.plot(t_plot,I,label='I')
    ax.plot(t_plot,R,label='R')
    ax.set_xlabel('Time')
    ax.set_ylabel('Population')
    ax.set_title(fig_title)
    ax.legend(loc='lower right')
    plt.savefig(file_name,dpi=100)


def main():
    betas = [3, 4, 5]
    gamma = 1
    N = 300000
    t_frame = 10
    delta_t = 0.25
    
    I0 = 300
    V0 = 150000
    VE = 0.8
    S0 = N - I0 - V0

    for beta in betas:
        anm_solns = get_ANM(S0, I0, V0, N, VE, beta, gamma, t_frame, delta_t)
        leaky_solns = get_leaky(S0, I0, V0, N, VE, beta, gamma, t_frame, delta_t)
        R0 = beta/gamma

        plot_vax_SIR(anm_solns[0], anm_solns[1], anm_solns[2], t_frame, delta_t, f'ANM, R0 = {int(R0)}', f'ANM_R0_{int(R0)}.png')
        plot_vax_SIR(leaky_solns[0], leaky_solns[1], leaky_solns[2], t_frame, delta_t, f'Leaky Model, R0 = {int(R0)}', f'Leaky_R0_{int(R0)}.png')


if __name__ == '__main__':
    main()
