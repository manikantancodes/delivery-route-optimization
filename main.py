import pandas as pd
from distance_calculator import calculate_distance_matrix
from tsp_optimizer import calculate_route_tsp
from visualize_route import visualize_route

# Load the delivery data
df = pd.read_csv('../data/delivery_data.csv')

# Extract coordinates
coordinates = df['Coordinates'].apply(eval).tolist()

# Calculate the distance matrix
dist_matrix = calculate_distance_matrix(coordinates)

# Solve the TSP problem to find the optimal route
optimal_route, total_distance = calculate_route_tsp(dist_matrix)

# Display the results
optimal_route_locations = [df['Location'].iloc[i] for i in optimal_route]
print(f"Optimal Route: {optimal_route_locations}")
print(f"Total Distance: {total_distance:.2f} km")

# Visualize the optimal route
visualize_route(optimal_route_locations, pd.DataFrame(dist_matrix, index=df['Location'], columns=df['Location']), df)
