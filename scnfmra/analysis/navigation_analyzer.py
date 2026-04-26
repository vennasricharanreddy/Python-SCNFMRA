import numpy as np

def distance_matrix(coords):
    arr = np.array(coords)
    diff = arr[:, None] - arr
    return np.sqrt((diff**2).sum(-1))