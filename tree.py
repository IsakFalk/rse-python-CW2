from math import cos, sin

from matplotlib import pyplot as plt

radius_length = 1
radius_multiplicative_update_factor = 0.6
theta_step_size = 0.1
num_steps = 5

x_init_start = 0.0
y_init_start = 0.0
x_init_end = 0.0
y_init_end = 1.0
theta_init = 0.0


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


current_leaves = [[x_init_end, y_init_end, theta_init]]
plt.plot([x_init_start, x_init_end], [y_init_start, y_init_end])
for steps in range(num_steps):
    new_leaves = []
    for current_leaf in current_leaves:
        new_leaf_left, new_leaf_right = grow_branches(
            current_leaf, radius_length, theta_step_size)
        plot_branch(current_leaf, new_leaf_left, new_leaf_right)
        append_left_right_leaves(new_leaves, new_leaf_left, new_leaf_right)

    current_leaves = new_leaves
    radius_length *= radius_multiplicative_update_factor
plt.savefig('tree.png')
