import math
import numpy as np

# Function that divide a open line segment defined by several points into uniform segments
# INPUTS:
# vertices: the vertices or points that form the line
# Sampling_distance: distance between the spected new points by following the curve

# OUTPUTS:
# new_points: the points that represent the new line

def open_line_uniform_segmetation(vertices, sampling_distance):
    new_vertices = np.empty([0, 3])
    new_edges = np.empty([0, 2], int)
    idx1 = 0
    # points1 = np.vstack([vertices, vertices[0,:]])
    points1 = vertices
    x = points1[:, 0]
    y = points1[:, 1]
    z = points1[:, 2]

    points = np.empty([0, 3])

    for i in range(len(x)-1):
        sample_points = 500
        points_act = np.linspace(start=points1[i, :], stop=points1[i+1, :], num=sample_points, endpoint=True)
        points = np.vstack([points, points_act])

    x = points[:, 0]
    y = points[:, 1]
    z = points[:, 2]

    tol = sampling_distance
    
    i, idx = 0, [0]
    points2 = points[0, :]

    while i < len(x):
        total_dist = 0
        for j in range(i + 1, len(x)):
            total_dist += math.sqrt((x[j] - x[j - 1]) ** 2 + (y[j] - y[j - 1]) ** 2 + (z[j] - z[j - 1]) ** 2)
            if total_dist >= tol:
                points2 = np.vstack([points2, [x[j], y[j], z[j]]])
                break
        i = j + 1
    new_vertices = np.vstack([new_vertices, points2])  # samples, edges and segments creation
    idx2 = len(new_vertices)

    if idx2 - 1 == idx1:
        new_edges = np.vstack([new_edges, [idx1, idx2]])
    else:
        for j in range(idx1, idx2 - 1, 1):
            new_edges = np.vstack([new_edges, [j, j + 1]])
    idx1 = idx2

    return new_vertices
