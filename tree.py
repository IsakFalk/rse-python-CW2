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

X_INDEX = 0
Y_INDEX = 1
THETA_INDEX = 2

LEFT_INDEX = -2
RIGHT_INDEX = -1

current_leaves = [[x_init_end, y_init_end, theta_init]]
plt.plot([x_init_start, x_init_end], [y_init_start, y_init_end])
for steps in range(num_steps):
    new_leaves = []
    for j in range(len(current_leaves)):
        new_leaves.append([current_leaves[j][X_INDEX]+radius_length*sin(current_leaves[j][THETA_INDEX]-theta_step_size),
                           current_leaves[j][Y_INDEX]+radius_length*cos(current_leaves[j][THETA_INDEX]-theta_step_size), current_leaves[j][THETA_INDEX]-theta_step_size])
        new_leaves.append([current_leaves[j][X_INDEX]+radius_length*sin(current_leaves[j][THETA_INDEX]+theta_step_size),
                           current_leaves[j][Y_INDEX]+radius_length*cos(current_leaves[j][THETA_INDEX]+theta_step_size), current_leaves[j][THETA_INDEX]+theta_step_size])
        plt.plot([current_leaves[j][X_INDEX], new_leaves[LEFT_INDEX][X_INDEX]],
                 [current_leaves[j][Y_INDEX], new_leaves[LEFT_INDEX][Y_INDEX]])
        plt.plot([current_leaves[j][X_INDEX], new_leaves[RIGHT_INDEX][X_INDEX]],
                 [current_leaves[j][Y_INDEX], new_leaves[RIGHT_INDEX][Y_INDEX]])
    current_leaves = new_leaves
    radius_length *= radius_multiplicative_update_factor
plt.savefig('tree.png')
