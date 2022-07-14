import numpy as np
# function to calcualte the angle between two 3d vectors
# INPUTS:
# vector 1 and vectro 2
# OUTPUTS:
# angel in radians 
# TODO: add degrees conversion


def angleBetweenVectors(vector_1, vector_2):
    unit_vector1 = vector_1 / np.linalg.norm(vector_1)
    unit_vector2 = vector_2 / np.linalg.norm(vector_2)
    # Because the dot product represents the cosine of the angle between two vectors.
    # a · b = |a| |b| cos(θ)
    dot_product = np.dot(unit_vector1, unit_vector2)
    # When the angle is more than π/2 then the cosine is negative, and the vectors point "away" from each other.
    # calculate the angle between two vectors
    angle = np.arccos(dot_product)
    return angle
