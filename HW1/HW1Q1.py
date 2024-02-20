import matplotlib
matplotlib.use('Agg')  # noqa
import matplotlib.pyplot as plt


def forward_euler(y0, delta_t, dydt):
    y_new = y0 + delta_t * dydt
    return y_new


def get_SIR_model(S0, I0, N, beta, gamma, t_frame):
    delta_t = 1  # day
    S = [S0]
    I = [I0]
    R = [N - S0 - I0]
    curr_S = S0
    curr_I = I0

    for t in range(t_frame):
        dSdt = -beta * curr_S * curr_I / N
        dIdt = beta * curr_S * curr_I / N - gamma * curr_I

        curr_S = forward_euler(curr_S, delta_t, dSdt)
        curr_I = forward_euler(curr_I, delta_t, dIdt)

        S.append(curr_S)
        I.append(curr_I)
        R.append(N - curr_S - curr_I)

    return S, I, R


def plot_SIR(S, I, R, t_frame, beta, gamma, fig_title):
    t_plot = list(range(0, t_frame + 1, 1))

    fig, ax = plt.subplots()
    ax.plot(t_plot,S,label='S Krista')
    ax.plot(t_plot,I,label='I Krista')
    ax.plot(t_plot,R,label='R Krista')
    ax.set_xlabel('Time')
    ax.set_ylabel('Population')
    ax.set_title(fig_title)
    ax.legend(loc='lower right')
    plt.savefig(fig_title,dpi=100)


def main():
    S0 = 999
    I0 = 1
    N = 1000
    t_frame = 50

    solns1 = get_SIR_model(S0, I0, N, 1, 0.5, t_frame)
    solns2 = get_SIR_model(S0, I0, N, 1.5, 0.5, t_frame)
    solns3 = get_SIR_model(S0, I0, N, 2, 0.5, t_frame)

    plot_SIR(solns1[0], solns1[1], solns1[2],
             t_frame, 1, 0.5, 'Q1_SIR1.png')
    plot_SIR(solns2[0], solns2[1], solns2[2],
             t_frame, 1.5, 0.5, 'Q1_SIR2.png')
    plot_SIR(solns3[0], solns3[1], solns3[2],
             t_frame, 2, 0.5, 'Q1_SIR3.png')


if __name__ == '__main__':
    main()