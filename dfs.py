# Function to perform DFS to find a path from start to target
def dfs(graph, start, target, path=None, visited=None):
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
    
    # Explore the neighbors of the current node
    for neighbor in graph[start]:
        # If the neighbor has not been visited yet, recurse deeper
        if neighbor not in visited:
            result = dfs(graph, neighbor, target, path, visited)
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

# Call the DFS function to find the path
path = dfs(graph, start_node, target_node)

# Print the result
if path:
    print(f"Path found from {start_node} to {target_node}: {path}")
else:
    print(f"No path found from {start_node} to {target_node}")
