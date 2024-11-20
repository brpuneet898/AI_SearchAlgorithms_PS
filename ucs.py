import heapq  # heapq is used to implement the priority queue

# Function to perform Uniform Cost Search (UCS)
def ucs(graph, start, target):
    # Priority queue to store nodes to explore along with their current path cost.
    # The queue will store tuples of the form (cost, node, path).
    priority_queue = []
    
    # Add the start node to the priority queue with a cost of 0 and an empty path.
    heapq.heappush(priority_queue, (0, start, []))
    
    # Set to keep track of visited nodes to avoid revisiting them
    visited = set()

    while priority_queue:
        # Get the node with the lowest cost from the priority queue
        cost, node, path = heapq.heappop(priority_queue)

        # If the node is the target, return the full path (start -> ... -> target) and its cost
        if node == target:
            return path + [node], cost
        
        # If the node has already been visited, skip it
        if node in visited:
            continue
        
        # Mark the current node as visited
        visited.add(node)
        
        # Explore the neighbors of the current node
        for neighbor, edge_cost in graph[node]:
            # If the neighbor has not been visited, add it to the priority queue
            if neighbor not in visited:
                heapq.heappush(priority_queue, (cost + edge_cost, neighbor, path + [node]))

    # If no path is found, return None
    return None, float('inf')  # No path found, return infinite cost


# Example graph represented as an adjacency list with edge weights.
# Each node has a list of tuples: (neighbor, cost)
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

# Starting and target nodes
start_node = 'A'
target_node = 'D'

# Call the UCS function to find the shortest path
path, cost = ucs(graph, start_node, target_node)

# Print the result
if path:
    print(f"Shortest path from {start_node} to {target_node}: {path} with total cost {cost}")
else:
    print(f"No path found from {start_node} to {target_node}")
