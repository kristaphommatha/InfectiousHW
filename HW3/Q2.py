import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def get_sir_compartmental(s0, i0, r0, Dp, Ds0, C, Dw_inv, Dy, delta_t, t_frame):
    s_dot = -(Ds0 @ Dp @ C @ Dw_inv) @ i0
    i_dot = (Ds0 @ Dp @ C @ Dw_inv) @ i0 - Dy @ i0
    r_dot = Dy @ i0

    t = 0
    s_pts = [s0]
    curr_s = s0
    i_pts = [i0]
    curr_i = i0
    r_pts = [r0]
    curr_r = r0
    curr_Ds = Ds0
    while t <= t_frame:
        curr_s = curr_s + delta_t * s_dot
        curr_i = curr_i + delta_t * i_dot
        curr_r = 1 - curr_s - curr_r
        curr_Ds = np.diag(curr_s.flatten())
        # print(f's, t = {t}')
        # print(curr_s)
        # print(f's_dot, t = {t}')
        # print(s_dot)

        s_pts.append(curr_s)
        i_pts.append(curr_i)
        r_pts.append(curr_r)

        s_dot = -(curr_Ds @ Dp @ C @ Dw_inv) @ curr_i
        i_dot = (curr_Ds @ Dp @ C @ Dw_inv) @ curr_i - Dy @ curr_i

        t = t + delta_t

    return s_pts, i_pts, r_pts


def Q2plotting(results, delta_t, t_frame, y_axis_title, fig_title, file_name):
    t_plot = [0]
    t = 0
    while t <= t_frame:
        t_plot.append(t)
        t = t + delta_t

    x1 = []
    x2 = []
    x3 = []
    x4 = []
    for x in results:
        x1.append(x[0].item())
        x2.append(x[1].item())
        x3.append(x[2].item())
        x4.append(x[3].item())

    fig, ax = plt.subplots()
    ax.plot(t_plot,x1,color='#b7dde6',label='Group 1')
    ax.plot(t_plot,x2,color='#92d1e0',label='Group 2')
    ax.plot(t_plot,x3,color='#41a6be',label='Group 3')
    ax.plot(t_plot,x4,color='#0e697f',label='Group 4')
    ax.set_xlabel('Time')
    ax.set_ylabel(y_axis_title)
    ax.set_title(fig_title)
    ax.legend(loc='upper right')
    plt.savefig(file_name,dpi=100)


def get_p_bar(p, s, delta_t, t_frame):
    p_bar = []
    for si in s:
        num = np.sum(np.multiply(p,si))
        den = np.sum(si)
        p_bar.append(num/den)
    return p_bar


def plot_p_bar(p, s, delta_t, t_frame):
    p_bar = get_p_bar(p,s,delta_t,t_frame)

    t_plot = [0]
    t = 0
    while t <= t_frame:
        t_plot.append(t)
        t = t + delta_t

    fig, ax = plt.subplots()
    ax.plot(t_plot,p_bar,color='black')
    ax.set_xlabel('Time')
    ax.set_ylabel('p_bar')
    ax.set_title('Weighted Avg. of Susceptibilities')
    plt.savefig('Q2d_p.png',dpi=100)


def main():
    c_bar = 0.45
    p = np.array([[1],[2],[3],[4]])
    s0 = np.full((4,1),0.999/4)
    i0 = np.full((4,1),0.001/4)
    r0 = np.full((4,1),0)

    Dp = np.diag(p.flatten())
    Ds0 = np.diag(s0.flatten())
    Dw_inv = np.array([[4,0,0,0],[0,4,0,0],[0,0,4,0],[0,0,0,4]])
    Dy = np.array([[3,0,0,0],[0,3,0,0],[0,0,3,0],[0,0,0,3]])
    C = np.full((4,4),c_bar)

    delta_t = 0.25
    t_frame = 10
    s_res, i_res, r_res = get_sir_compartmental(s0, i0, r0,
                                                Dp, Ds0, C, Dw_inv, Dy,
                                                delta_t, t_frame)

    Q2plotting(i_res,delta_t,t_frame,'Infectioned Population Proportion','Infections vs. Time','Q2c.png')
    Q2plotting(s_res,delta_t,t_frame,'Susceptible Population Proportion','Susceiptibles vs. Time','Q2d_s.png')
    plot_p_bar(p,s_res,delta_t,t_frame)


if __name__ == '__main__':
    main()
