# You are given a grid with cells that have a cost of moving through them. The goal is to find the shortest path from a starting point to a target point using the Local Beam Search algorithm.

# A helper function for calculating the Manhattan distance heuristic (h) between two points
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# Local Beam Search algorithm
def local_beam_search(grid, start, target, beam_width=2, max_iterations=100):
    # Each path is a list of nodes from start to current position
    # Start with a list of k initial paths (here just starting at the start node)
    paths = [[start]]

    for iteration in range(max_iterations):
        # Generate all possible next states from the current paths
        next_paths = []
        for path in paths:
            current_node = path[-1]
            neighbors = []

            # Explore neighbors (up, down, left, right)
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Possible moves: up, down, left, right

            for direction in directions:
                neighbor = (current_node[0] + direction[0], current_node[1] + direction[1])

                # Ensure the neighbor is within bounds of the grid
                if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]):
                    # Create a new path by appending the neighbor to the current path
                    new_path = list(path)
                    new_path.append(neighbor)
                    neighbors.append(new_path)

            # Add all generated neighbors to the next_paths list
            next_paths.extend(neighbors)

        # Rank the paths based on the heuristic cost (f = g + h) and select the best `k` paths
        next_paths = sorted(next_paths, key=lambda x: len(x) + heuristic(x[-1], target))[:beam_width]

        # If one of the best paths has reached the target, return it
        for path in next_paths:
            if path[-1] == target:
                return path

        # Update the paths for the next iteration
        paths = next_paths

    # If no path is found within the maximum iterations, return an empty list
    return []

# Example grid (cost to move through each cell)
grid = [
    [1, 2, 1, 10],
    [1, 2, 1, 1],
    [1, 1, 1, 1],
    [10, 1, 1, 1]
]

start_node = (0, 0)  # Top-left corner
target_node = (1, 3)  # Bottom-right corner
beam_width = 2  # The number of best paths to keep in memory at each iteration
max_iterations = 100  # Maximum number of iterations
shortest_path = local_beam_search(grid, start_node, target_node, beam_width, max_iterations)

print("Shortest path from", start_node, "to", target_node, ":", shortest_path)
