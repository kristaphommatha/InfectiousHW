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


def plot_vax_SIR(ANM, leaky, t_frame, delta_t, R0, file_name):
    t = 0
    t_plot = [t]
    while t <= t_frame:
        t_plot.append(t)
        t = t + delta_t

    fig, axes = plt.subplots(1,2)
    fig.set_size_inches(12.5, 5)
    axes[0].plot(t_plot,ANM[0],label='S')
    axes[0].plot(t_plot,ANM[1],label='I')
    axes[0].plot(t_plot,ANM[2],label='R')
    axes[0].set_xlabel('Time')
    axes[0].set_ylabel('Population')
    axes[0].set_title(f'ANM, R0 = {R0}')
    axes[0].legend(loc='lower right')
    axes[0].spines[['right', 'top']].set_visible(False)
    axes[0].set_ylim(0,max(leaky[2])+1000)

    axes[1].plot(t_plot,leaky[0],label='S')
    axes[1].plot(t_plot,leaky[1],label='I')
    axes[1].plot(t_plot,leaky[2],label='R')
    axes[1].set_xlabel('Time')
    axes[1].set_ylabel('Population')
    axes[1].set_title(f'Leaky Model, R0 = {R0}')
    axes[1].legend(loc='lower right')
    axes[1].spines[['right', 'top']].set_visible(False)
    axes[1].set_ylim(0,max(leaky[2])+1000)
    
    plt.savefig(file_name,dpi=100)


def main():
    betas = [3, 4, 5]
    gamma = 1
    N = 300000
    t_frame = 20
    delta_t = 0.25
    
    I0 = 300
    V0 = 150000
    VE = 0.8
    S0 = N - I0 - V0

    for beta in betas:
        anm_solns = get_ANM(S0, I0, V0, N, VE, beta, gamma, t_frame, delta_t)
        leaky_solns = get_leaky(S0, I0, V0, N, VE, beta, gamma, t_frame, delta_t)
        R0 = int(beta/gamma)

        plot_vax_SIR(anm_solns,leaky_solns,t_frame,delta_t,R0,f'Q2c_R0-{R0}.png')


if __name__ == '__main__':
    main()
