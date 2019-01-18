from math import cos, sin

from matplotlib import pyplot as plt

radius_length = 1
current_leaves = [[0, 1, 0]]
plt.plot([0, 0], [0, 1])
for steps in range(5):
    new_leaves = []
    for j in range(len(current_leaves)):
        new_leaves.append([current_leaves[j][0]+radius_length*sin(current_leaves[j][2]-0.1),
                           current_leaves[j][1]+radius_length*cos(current_leaves[j][2]-0.1), current_leaves[j][2]-0.1])
        new_leaves.append([current_leaves[j][0]+radius_length*sin(current_leaves[j][2]+0.1),
                           current_leaves[j][1]+radius_length*cos(current_leaves[j][2]+0.1), current_leaves[j][2]+0.1])
        plt.plot([current_leaves[j][0], new_leaves[-2][0]],
                 [current_leaves[j][1], new_leaves[-2][1]])
        plt.plot([current_leaves[j][0], new_leaves[-1][0]],
                 [current_leaves[j][1], new_leaves[-1][1]])
    current_leaves = new_leaves
    radius_length *= 0.6
plt.savefig('tree.png')
