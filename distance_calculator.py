import numpy as np
from scipy.spatial import distance_matrix

def calculate_distance_matrix(coordinates):
    """
    Calculate the distance matrix between delivery locations.

    Parameters:
    coordinates (list of tuples): List of latitude and longitude for each location.

    Returns:
    np.ndarray: A distance matrix.
    """
    return distance_matrix(coordinates, coordinates)
