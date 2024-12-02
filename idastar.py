# You are given a grid with cells that have a cost of moving through them. The goal is to find the shortest path from a starting point to a target point using the IDA* algorithm.

# A helper function for calculating the Manhattan distance heuristic (h) between two points
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# IDA* algorithm
def idastar(grid, start, target):
    # A helper function to perform the search with a given limit
    def search(node, g, path, limit):
        f = g + heuristic(node, target)  # Calculate f = g + h

        if f > limit:
            return f  # Return the f value if it's above the limit (prune this path)

        if node == target:
            return path  # Found the target, return the path

        min_f = float('inf')
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Possible moves: up, down, left, right
        
        # Explore neighbors
        for direction in directions:
            neighbor = (node[0] + direction[0], node[1] + direction[1])

            # Ensure the neighbor is within bounds of the grid
            if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]):
                # Skip already visited nodes in the current path (to avoid cycles)
                if neighbor not in path:
                    new_path = path + [neighbor]
                    result = search(neighbor, g + grid[neighbor[0]][neighbor[1]], new_path, limit)
                    if isinstance(result, list):  # If a valid path is returned
                        return result
                    min_f = min(min_f, result)  # Otherwise, update the minimum f value

        return min_f  # Return the minimum f value encountered during the search

    limit = heuristic(start, target)  # Start with the heuristic as the initial limit
    while True:
        result = search(start, 0, [start], limit)
        if isinstance(result, list):  # Found the path
            return result
        if result == float('inf'):  # No solution found within the current limit
            return []  # No solution exists
        limit = result  # Increase the limit and try again

# Example grid (cost to move through each cell)
grid = [
    [1, 2, 1, 10],
    [1, 2, 1, 1],
    [1, 1, 1, 1],
    [10, 1, 1, 1]
]

start_node = (0, 0)  # Top-left corner
target_node = (3, 3)  # Bottom-right corner
shortest_path = idastar(grid, start_node, target_node)

print("Shortest path from", start_node, "to", target_node, ":", shortest_path)
