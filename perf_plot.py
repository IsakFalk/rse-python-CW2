import argparse
import time

import matplotlib.pyplot as plt
import numpy as np

import tree

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--num_steps", type=int,
                        help="number of steps to grow the tree for",
                        default=5)
    parser.add_argument("-dt", "--theta_step_size",
                        type=float, help="step size of theta",
                        default=0.1)
    parser.add_argument("-r", "--radius_length", type=float,
                        help="starting radius length",
                        default=1.0)
    parser.add_argument("-m", "--radius_multiplicative_update_factor",
                        type=float, help="factor to multiply radius with at each iteration",
                        default=0.6)
    args = parser.parse_args()

    num_steps = args.num_steps
    theta_step_size = args.theta_step_size
    radius_length = args.radius_length
    radius_multiplicative_update_factor = args.radius_multiplicative_update_factor

    # row 0: walltime vs number of iterations
    # row 1: semilogy version of plot in row 1
    fig, ax = plt.subplots(2, 1, figsize=(12, 12), sharex=True)

    # list solution
    max_steps = 18

    t = []
    x = np.arange(1, max_steps + 1)
    for num_steps in range(1, max_steps+1):
        start_time = time.time()
        tree.build_tree(num_steps, theta_step_size, radius_length,
                        radius_multiplicative_update_factor, plot=False)
        end_time = time.time()
        walltime = end_time - start_time
        t.append(walltime)
    t = np.array(t)

    # plot x vs t
    ax[0].plot(x, t, color='g', label='empirical data (tree.py)')

    # plot x vs log(t)
    A = np.vstack([x[t > 0], np.ones(len(x[t > 0]))]).T
    k, m = np.linalg.lstsq(A, np.log2(t[t > 0]), rcond=None)[0]

    ax[1].semilogy(x, t, label='empirical data (tree.py)',
                   color='g', linestyle='', basey=2)
    ax[1].plot(x[t > 0], 2 ** (k*x[t > 0] + m),
               color='cyan', marker='',
               label='lsq (tree.py): log2(f(n)) = {:.4f}*n + {:.4f}'.format(k, m))

    # Style graph
    ax[0].set_ylabel('Walltime (seconds)')
    ax[0].legend()
    ax[1].set_xlabel('Number of iterations')
    ax[1].set_ylabel('Walltime (seconds)')
    ax[1].legend()

    plt.tight_layout()
    fig.savefig('perf_plot.png')
    plt.close('all')
