import argparse
from math import cos, sin

from matplotlib import pyplot as plt


def grow_branches(leaf, radius_length, theta_step_size):
    x, y, theta = leaf
    new_theta_left = theta - theta_step_size
    new_theta_right = theta + theta_step_size
    new_x_left = x + radius_length*sin(new_theta_left)
    new_x_right = x + radius_length*sin(new_theta_right)
    new_y_left = y + radius_length*cos(new_theta_left)
    new_y_right = y + radius_length*cos(new_theta_right)

    new_leaf_left = [new_x_left, new_y_left, new_theta_left]
    new_leaf_right = [new_x_right, new_y_right, new_theta_right]
    return new_leaf_left, new_leaf_right


def append_left_right_leaves(new_leaves, new_leaf_left, new_leaf_right):
    new_leaves.append(new_leaf_left)
    new_leaves.append(new_leaf_right)


def plot_branch(current_leaf, new_leaf_left, new_leaf_right):
    x, y, _ = current_leaf
    new_x_left, new_y_left, _ = new_leaf_left
    new_x_right, new_y_right, _ = new_leaf_right

    plt.plot([x, new_x_left],
             [y, new_y_left])
    plt.plot([x, new_x_right],
             [y, new_y_right])


def build_tree(num_steps, theta_step_size, radius_length, radius_multiplicative_update_factor,
               theta_init=0, x_init_start=0.0, y_init_start=0.0, x_init_end=0.0, y_init_end=1.0,
               plot=True):
    if plot:
        plt.plot([x_init_start, x_init_end], [y_init_start, y_init_end])
    current_leaves = [[x_init_end, y_init_end, theta_init]]

    for step in range(num_steps):
        new_leaves = []
        for current_leaf in current_leaves:
            new_leaf_left, new_leaf_right = grow_branches(
                current_leaf, radius_length, theta_step_size)
            if plot:
                plot_branch(current_leaf, new_leaf_left, new_leaf_right)
            append_left_right_leaves(
                new_leaves, new_leaf_left, new_leaf_right)

        current_leaves = new_leaves
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
    plt.savefig('tree.png')
