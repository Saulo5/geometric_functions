# Function that find the closest point in a line with respect to a given point
# imports
import numpy as np
# INPUTS
# pt1 = initial point on a line
# pt2 = end point in a line
# p = The point to validate
# OUTPUTS
# clsst_point = the closest point in line to a point p 

def ClosestPointOnLine(a, b, p):
    ap = p-a
    ab = b-a
    clsst_point = a + np.dot(ap,ab)/np.dot(ab,ab) * ab
    return clsst_point
# some reference for the maths: https://math.stackexchange.com/questions/3518495/check-if-a-general-point-is-inside-a-given-cylinder
