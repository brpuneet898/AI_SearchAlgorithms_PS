# Function to perform Depth Limited Search to find a path from start to target
def dls(graph, start, target, limit, path=None, visited=None):
    # Initialize the path and visited set if they are not provided
    if path is None:
        path = []
    if visited is None:
        visited = set()

    # Add the current node to the path and visited set
    path.append(start)
    visited.add(start)

    # If we found the target, return the path
    if start == target:
        return path

    # If the depth limit is reached, stop further exploration
    if limit == 0:
        return None

    # Explore the neighbors of the current node
    for neighbor in graph[start]:
        # If the neighbor has not been visited yet, recurse deeper with reduced limit
        if neighbor not in visited:
            result = dls(graph, neighbor, target, limit - 1, path, visited)
            # If a valid path is found, return it
            if result:
                return result

    # If no path is found, return None
    return None

# Example graph represented as an adjacency list
graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0, 3],
    3: [1, 2]
}

# Starting and target nodes
start_node = 0
target_node = 3
# Depth limit for the search
depth_limit = 1

# Call the DLS function to find the path
path = dls(graph, start_node, target_node, depth_limit)

# Print the result
if path:
    print(f"Path found from {start_node} to {target_node}: {path}")
else:
    print(f"No path found from {start_node} to {target_node} within depth limit {depth_limit}")
