import HW2Q1a as Q1a
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def find_max_err(s0, i0, beta, gamma, t_frame, delta_t):
    e_s, e_i = Q1a.get_sis_model(s0, i0, beta, gamma, t_frame, delta_t)
    a_i = Q1a.get_analytical_i(i0, beta, gamma, t_frame, delta_t)
    error_list = []
    for e,a in zip(e_i, a_i):
        err = abs(e - a)
        error_list.append(err)
    return max(error_list)


def main():
    beta = 3
    gamma = 2
    s0 = 0.99
    i0 = 1 - s0
    t_frame = 25

    powers = [1, 0, -1, -2, -3, -4, -5]
    delta_ts = []
    error_list = []
    for p in powers:
        delta_ts.append(2**p)

    for delta_t in delta_ts:
        error_list.append(find_max_err(s0, i0, beta, gamma, t_frame, delta_t))

    fig, ax = plt.subplots()
    ax.plot(delta_ts, error_list)
    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.set_xlabel('delta_t')
    ax.set_ylabel('Maximum Error')
    ax.set_title(f'Maximum Error vs. delta_t')
    plt.savefig('Q1d.png',dpi=100)


if __name__ == '__main__':
    main()