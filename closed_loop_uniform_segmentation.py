import math
import numpy as np
import open3d as o3d
from scipy.spatial import ConvexHull
import scipy.interpolate as si

# Function that divide a closed line segment defined by several points into uniform segments
# INPUTS:
# vertices: the vertices or points that form the line
# edges: the conectivity list between points
# num_points: the number of points to represent the new line

# OUTPUTS:
# new_points: the points that represent the new line
# new_edges: the new st of segments that conform the line


def line_uniform_segmetation(vertices, edges, num_points):
    new_vertices = np.empty([0, 3])
    new_edges = np.empty([0, 2], int)
    idx1 = 0
    points1 = np.vstack([vertices, vertices[0,:]])
    x = points1[:, 0]
    y = points1[:, 1]
    z = points1[:, 2]

    points = scipy_bspline(points1, 2000, len(points1)-1, periodic=True)
    x = points[:, 0]
    y = points[:, 1]
    z = points[:, 2]

    # calcualte the perimeter of the shape
    perimeter = 0
    for k in range(1, len(x)):
        perimeter += math.sqrt((x[k] - x[k - 1]) ** 2 + (y[k] - y[k - 1]) ** 2 + (z[k] - z[k - 1]) ** 2)
    # calculate the distance between points give a number of points
    sampling_distance = perimeter / (num_points)
    tol = sampling_distance
    # print(tol)
    # print(perimeter / tol)

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
    points2 = np.vstack([points2, points[-1, :]])
    # points2 = np.vstack([points2, points[0, :]])
    new_vertices = np.vstack([new_vertices, points2])  # samples, edges and segments creation
    idx2 = len(new_vertices)

    if idx2 - 1 == idx1:
        new_edges = np.vstack([new_edges, [idx1, idx2]])
    else:
        for j in range(idx1, idx2 - 1, 1):
            new_edges = np.vstack([new_edges, [j, j + 1]])
    idx1 = idx2


    return new_vertices, new_edges


# line fitting B-spline
def scipy_bspline(cv, n, degree, periodic=False):
    """ Calculate n samples on a bspline
        cv :      Array ov control vertices
        n  :      Number of samples to return
        degree:   Curve degree
        periodic: True - Curve is closed
    """
    cv = np.asarray(cv)
    count = cv.shape[0]

    # Closed curve
    if periodic:
        kv = np.arange(-degree,count+degree+1)
        factor, fraction = divmod(count+degree+1, count)
        cv = np.roll(np.concatenate((cv,) * factor + (cv[:fraction],)),-1,axis=0)
        degree = np.clip(degree,1,degree)

    # Opened curve
    else:
        degree = np.clip(degree,1,count-1)
        kv = np.clip(np.arange(count+degree+1)-degree, 0, count-degree)
    # Return samples
    max_param = count - (degree * (1-periodic))
    spl = si.BSpline(kv, cv, degree)
    return spl(np.linspace(0, max_param, n))
