# Depth Limited Search (DLS) function used by IDDFS
def dls(graph, start, target, limit, path=None, visited=None):
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
            if result:
                return result

    # If no path is found, return None
    return None


# Iterative Deepening DFS (IDDFS) function
def iddfs(graph, start, target):
    # Start with depth limit 0 and keep increasing it
    depth = 0
    while True:
        print(f"Searching at depth {depth}...")  # Just to show the current depth
        path = dls(graph, start, target, depth)

        # If a path is found, return it
        if path:
            return path
        
        # Increment the depth limit for the next iteration
        depth += 1

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

# Call the IDDFS function to find the path
path = iddfs(graph, start_node, target_node)

# Print the result
if path:
    print(f"Path found from {start_node} to {target_node}: {path}")
else:
    print(f"No path found from {start_node} to {target_node}")
