import sys
sys.path.insert(0, '../HW1')
import HW1Q1 as HW1Q1

def get_sis_model(s0, i0, beta, gamma, t_frame, delta_t):
    s = [s0]
    i = [i0]
    curr_s = s0
    curr_i = i0
    t = 0

    while t <= t_frame:
        dsdt = -beta * curr_s * curr_i + gamma * curr_i
        dIdt = beta * curr_s * curr_i - gamma * curr_i

        curr_s = forward_euler(curr_s, delta_t, dsdt)
        curr_i = forward_euler(curr_i, delta_t, didt)

        s.append(curr_s)
        i.append(curr_i)
        t = t + delta_t

    return s, i


def get_analytical_i(i0, beta, gamma, t_frame, delta_t):
    R0 = beta/gamma
    i = [i0]
    while t <= t_frame:
        new_i = (1 - 1/R0)/(1+(1-1/R0-i0)/i0 * exp(-(beta-gamma)*t))
        i.append(new_i)
        t = t + delta_t

    return i
