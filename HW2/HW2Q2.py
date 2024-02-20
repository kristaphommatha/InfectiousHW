import sys
sys.path.insert(0, '../HW1')
import HW1Q1 as HW1Q1
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import math


def get_ANM(S0, I0, V0, VE, beta, gamma, t_frame, delta_t):
    S = [S0]
    I = [I0]
    Vo = [(1 - VE)*V0]
    R = [N - S0 - I0 - V0]
    curr_S = S0
    curr_I = I0
    curr_Vo = (1 - VE)*V0

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
        R.append(N - curr_S - curr_I - curr_Vo)

        t = t + delta_t

    return S, I, Vo, R
