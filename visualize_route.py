import networkx as nx
import matplotlib.pyplot as plt

def visualize_route(route, dist_df, locations):
    """
    Visualize the optimal delivery route.

    Parameters:
    route (list): List of locations in the optimized route.
    dist_df (pd.DataFrame): DataFrame containing the distances between locations.
    locations (pd.DataFrame): The original dataset with location coordinates.

    Returns:
    None
    """
    G = nx.Graph()

    for loc in locations['Location']:
        G.add_node(loc)

    for i in range(len(route) - 1):
        G.add_edge(route[i], route[i+1])

    plt.figure(figsize=(10, 8))
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', font_size=10, node_size=5000, font_weight='bold')

    edge_labels = {(route[i], route[i+1]): 
                   f"{dist_df[route[i]][route[i+1]]:.2f} km" 
                   for i in range(len(route) - 1)}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

    plt.title("Optimized Delivery Route")
    plt.show()
