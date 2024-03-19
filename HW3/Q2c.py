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


def main():
    c_bar = 0.45
    s0 = np.full((4,1),0.999/4)
    i0 = np.full((4,1),0.001/4)
    r0 = np.full((4,1),0)

    Dp = np.array([[1,0,0,0],[0,2,0,0],[0,0,3,0],[0,0,0,4]])
    Ds0 = np.diag(s0.flatten())
    Dw_inv = np.array([[4,0,0,0],[0,4,0,0],[0,0,4,0],[0,0,0,4]])
    Dy = np.array([[3,0,0,0],[0,3,0,0],[0,0,3,0],[0,0,0,3]])
    C = np.full((4,4),c_bar)

    delta_t = 0.25
    t_frame = 10
    s_res, i_res, r_res = get_sir_compartmental(s0, i0, r0,
                                                Dp, Ds0, C, Dw_inv, Dy,
                                                delta_t, t_frame)

    t_plot = [0]
    t = 0
    while t <= t_frame:
        t_plot.append(t)
        t = t + delta_t

    i1 = []
    i2 = []
    i3 = []
    i4 = []
    for x in i_res:
        i1.append(x[0].item())
        i2.append(x[1].item())
        i3.append(x[2].item())
        i4.append(x[3].item())

    fig, ax = plt.subplots()
    ax.plot(t_plot,i1,color='#b7dde6',label='Group 1')
    ax.plot(t_plot,i2,color='#92d1e0',label='Group 2')
    ax.plot(t_plot,i3,color='#41a6be',label='Group 3')
    ax.plot(t_plot,i4,color='#0e697f',label='Group 4')
    ax.set_xlabel('Time')
    ax.set_ylabel('Infected Population Proportion')
    ax.set_title('Infections vs. Time')
    ax.legend(loc='lower right')
    plt.savefig('Q2c.png',dpi=100)


if __name__ == '__main__':
    main()
