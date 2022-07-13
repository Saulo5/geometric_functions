# function to determine if a set of points are inside a cylinder defined by 2 points (central axis) and a radius
# imports
import numpy as np
# INPUTS:
# pt1 = point 1 of the axis. pt1 = [x1, y1, z1]
# pt2 = point 2 of the axis. pt2 = [x2, y2, z2]
# r = cylinder radius
# q = set of points to validate if they are inside or outside the cylinder
# OUTPUTS:
# index: the index of points in q that are inside
# points_inside = the points inside the cylinder

def points_in_cylinder(pt1, pt2, r, q):
    vec = pt2 - pt1 # vector that represents the cylinder axis
    # validate if points are inside the two planes that forms the cylinder
    cond1 = np.asarray(np.where(np.dot(q - pt1, vec) >= 0))
    cond2 = np.asarray(np.where(np.dot(q - pt2, vec) <= 0))
    # calculate the distance from points to line and keep anly the ones inside the radius limit
    a = np.linalg.norm(np.cross(q - pt1, vec), axis = 1)
    b = np.linalg.norm(vec)
    cond3 = np.asarray(np.where((a/b)<=r))
    # keep only the points that satysfied condition 1, 2 and 3.
    idx_1 = np.intersect1d(cond1,cond3)
    index = np.intersect1d(idx_1, cond2) # return the index of the points that are inside the cylinder
    points_inside = q[idx, :] #points inside
    
    return index, points_inside
  
# some reference to the maths: https://math.stackexchange.com/questions/3518495/check-if-a-general-point-is-inside-a-given-cylinder
