from itertools import permutations

def calculate_route_tsp(dist_matrix):
    """
    Calculate the shortest route using a brute-force TSP approach.

    Parameters:
    dist_matrix (np.ndarray): A 2D array representing the distances between locations.

    Returns:
    tuple: The optimal route and the total distance.
    """
    num_locations = len(dist_matrix)
    locations = range(1, num_locations)
    
    shortest_route = None
    min_distance = float('inf')

    for route in permutations(locations):
        current_route = [0] + list(route) + [0]
        distance = sum(dist_matrix[current_route[i], current_route[i+1]] for i in range(num_locations))
        
        if distance < min_distance:
            min_distance = distance
            shortest_route = current_route
    
    return shortest_route, min_distance
