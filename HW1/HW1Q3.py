import numpy as np
from scipy.optimize import fsolve
import matplotlib
matplotlib.use('Agg')  # noqa
import matplotlib.pyplot as plt


def equation(r, R0):
    return r - (1 - np.exp(-r*R0))


def find_intersection(R0_array):
    intersect_list = []
    for R0 in R0_array:
        initial_guess = [0.5, 0.5]
        intersect = fsolve(equation, initial_guess, args=(R0,))
        intersect_list.append(intersect)
    return intersect_list


def main():
    R0_array = [0.9, 1.0, 1.1, 1.2]
    r_span = r_span = [x/100 for x in range(0, 50, 5)]
    f = []
    g1 = []
    g2 = []
    g3 = []
    g4 = []
    for r in r_span:
        f.append(r)
        g1.append(1 - np.exp(-R0_array[0]*r))
        g2.append(1 - np.exp(-R0_array[1]*r))
        g3.append(1 - np.exp(-R0_array[2]*r))
        g4.append(1 - np.exp(-R0_array[3]*r))
        
    pts = find_intersection(R0_array)

    fig, axes = plt.subplots(2,2)
    fig.set_size_inches(10, 10)

    axes[0,0].scatter(pts[0][0],pts[0][1], zorder = 3)
    axes[0,0].plot(r_span, f, color='black', label='f')
    axes[0,0].plot(r_span, g1, color='red', label='g')
    axes[0,0].set_xlabel('r')
    axes[0,0].set_ylabel('r_infinity')
    axes[0,0].set_title('R0 = 0.9')
    axes[0,0].spines[['right', 'top']].set_visible(False)
    
    axes[0,1].scatter(pts[1][0],pts[1][1], zorder = 3)
    axes[0,1].plot(r_span, f, color='black', label='f')
    axes[0,1].plot(r_span, g2, color='red', label='g')
    axes[0,1].set_xlabel('r')
    axes[0,1].set_ylabel('r_infinity')
    axes[0,1].set_title('R0 = 1.0')
    axes[0,1].spines[['right', 'top']].set_visible(False)
    
    axes[1,0].scatter(pts[2][0],pts[2][1], zorder = 3)
    axes[1,0].plot(r_span, f, color='black', label='f')
    axes[1,0].plot(r_span, g3, color='red', label='g')
    axes[1,0].set_xlabel('r')
    axes[1,0].set_ylabel('r_infinity')
    axes[1,0].set_title('R0 = 1.1')
    axes[1,0].spines[['right', 'top']].set_visible(False)
    
    axes[1,1].scatter(pts[3][0],pts[3][1], zorder = 3)
    axes[1,1].plot(r_span, f, color='black', label='f')
    axes[1,1].plot(r_span, g4, color='red', label='g')
    axes[1,1].set_xlabel('r')
    axes[1,1].set_ylabel('r_infinity')
    axes[1,1].set_title('R0 = 1.2')
    axes[1,1].spines[['right', 'top']].set_visible(False)
    
    plt.savefig('Q3b.png',dpi=100)


if __name__ == '__main__':
    main()