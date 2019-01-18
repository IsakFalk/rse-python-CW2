import argparse

import numpy as np
from matplotlib import pyplot as plt


def grow_branches(current_leaves, radius_length, theta_steps):
    # new_leaves is an array which looks like a (-1, 3, 2) cube
    # where (-1) represents the current number of leaves.
    # the second row is the (x, y, theta) columns of the states.
    # Finally, the last two indices are such that
    # new_leaves[:, :, 0] are the new states to the left of the current_leaves
    # new_leaves[:, :, 0] are the new states to the right of the current_leaves
    new_leaves = np.empty((*current_leaves.shape, 2))
    # numpy broadcasts the current_leaves array to fit into the shape of new_leaves
    # automatically.
    new_leaves[:, 2, :] = current_leaves[:,
                                         2].reshape(-1, 1) - theta_steps.reshape(1, -1)
    new_leaves[:, 0, :] = current_leaves[:,
                                         0].reshape(-1, 1) + radius_length * np.sin(new_leaves[:, 2, :])
    new_leaves[:, 1, :] = current_leaves[:,
                                         1].reshape(-1, 1) + radius_length * np.cos(new_leaves[:, 2, :])
    return new_leaves


def interleave_branches(new_leaves):
    # Interleave the two new matrices representing state.
    # This makes sure the plot stays the same as we draw the lines
    # in the same order as in the original tree.py
    interleaved_leaves = np.empty(
        (2 * new_leaves.shape[0], 3), dtype=new_leaves.dtype)
    interleaved_leaves[0::2] = new_leaves[:, :, 0]
    interleaved_leaves[1::2] = new_leaves[:, :, 1]
    return interleaved_leaves


def plot_branches(current_leaves, new_leaves):
    for i, leaves in enumerate(current_leaves):
        # plot left branch
        plt.plot([leaves[0], new_leaves[i, 0, 0]],
                 [leaves[1], new_leaves[i, 1, 0]])
        # plot right branch
        plt.plot([leaves[0], new_leaves[i, 0, 1]],
                 [leaves[1], new_leaves[i, 1, 1]])


def build_tree(num_steps, theta_step_size, radius_length, radius_multiplicative_update_factor,
               theta_init=0, x_init_start=0.0, y_init_start=0.0, x_init_end=0.0, y_init_end=1.0,
               plot=True):
    if plot:
        plt.plot([x_init_start, x_init_end], [y_init_start, y_init_end])
    current_leaves = np.array([[x_init_end, y_init_end, theta_init]])
    theta_steps = np.array([theta_step_size, -theta_step_size])
    for step in range(num_steps):
        new_leaves = grow_branches(current_leaves, radius_length, theta_steps)
        if plot:
            plot_branches(current_leaves, new_leaves)
        current_leaves = interleave_branches(new_leaves)
        radius_length *= radius_multiplicative_update_factor


if __name__ == "__main__":
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

    build_tree(num_steps, theta_step_size, radius_length,
               radius_multiplicative_update_factor)
    plt.savefig('tree_np.png')
