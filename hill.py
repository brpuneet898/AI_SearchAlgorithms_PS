# You are given a grid with cells that have a cost of moving through them. The goal is to find the shortest path from a starting point to a target point using the Hill Climbing algorithm.

# A helper function for calculating the Manhattan distance heuristic (h) between two points
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# Hill Climbing algorithm
def hill_climbing(grid, start, target):
    # Start with the initial node as the current node
    current_node = start
    path = [current_node]

    while current_node != target:
        neighbors = []

        # Explore neighbors (up, down, left, right)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Possible moves: up, down, left, right

        for direction in directions:
            neighbor = (current_node[0] + direction[0], current_node[1] + direction[1])

            # Ensure the neighbor is within bounds of the grid
            if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]):
                neighbors.append(neighbor)

        # If no valid neighbors, exit as there is no solution
        if not neighbors:
            return []

        # Choose the neighbor with the best heuristic value (nearest to the target)
        best_neighbor = None
        best_heuristic = float('inf')

        for neighbor in neighbors:
            h_value = heuristic(neighbor, target)  # Calculate heuristic value

            if h_value < best_heuristic:
                best_heuristic = h_value
                best_neighbor = neighbor

        # If we can't find a better neighbor, we are stuck at a local optimum
        if heuristic(best_neighbor, target) >= heuristic(current_node, target):
            return path  # Return the current path as we've reached a local optimum

        # Move to the best neighbor
        current_node = best_neighbor
        path.append(current_node)

    return path  # Return the path when the target is reached

# Example grid (cost to move through each cell)
grid = [
    [1, 2, 1, 10],
    [1, 2, 1, 1],
    [1, 1, 1, 1],
    [10, 1, 1, 1]
]

start_node = (0, 0)  # Top-left corner
target_node = (3, 1)  # Bottom-right corner
shortest_path = hill_climbing(grid, start_node, target_node)

print("Shortest path from", start_node, "to", target_node, ":", shortest_path)
