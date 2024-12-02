# You are given a grid with cells that have a cost of moving through them. The goal is to find the shortest path from a starting point to a target point using the Recursive Best-First Search (RBFS) algorithm.

# A helper function for calculating the Manhattan distance heuristic (h) between two points
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# Recursive Best-First Search (RBFS) algorithm
def rbfs(grid, start, target, limit=float('inf')):
    # A helper function to perform the search with a given limit (best-first)
    def search(node, g, path, f_limit):
        f = g + heuristic(node, target)  # Calculate f = g + h (heuristic cost)

        if f > f_limit:
            return float('inf')  # If the f value is above the limit, return infinity (prune)

        if node == target:
            return path  # If the target is reached, return the current path

        # Explore the neighbors (up, down, left, right)
        neighbors = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Possible moves: up, down, left, right

        for direction in directions:
            neighbor = (node[0] + direction[0], node[1] + direction[1])

            # Ensure the neighbor is within bounds of the grid
            if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]):
                if neighbor not in path:  # Avoid revisiting nodes in the current path
                    neighbors.append(neighbor)

        if not neighbors:  # No valid neighbors
            return float('inf')  # Return infinity if no neighbors to expand

        # Sort neighbors based on their f value (g + h)
        neighbors = sorted(neighbors, key=lambda x: g + grid[x[0]][x[1]] + heuristic(x, target))

        best = float('inf')
        for i in range(len(neighbors)):
            # Limit is the smallest f value of the neighbors
            new_f_limit = best if i == len(neighbors) - 1 else min(best, f + grid[neighbors[i][0]][neighbors[i][1]] + heuristic(neighbors[i], target))
            result = search(neighbors[i], g + grid[neighbors[i][0]][neighbors[i][1]], path + [neighbors[i]], new_f_limit)

            if isinstance(result, list):
                return result  # Found a valid path
            best = min(best, result)

        return best  # Return the best f value found

    # Start the search from the start node
    result = search(start, 0, [start], limit)

    if isinstance(result, list):  # Found the path
        return result
    return []  # No path found

# Example grid (cost to move through each cell)
grid = [
    [1, 2, 1, 10],
    [1, 2, 1, 1],
    [1, 1, 1, 1],
    [10, 1, 1, 1]
]

start_node = (0, 0)  # Top-left corner
target_node = (2, 3)  # Bottom-right corner
shortest_path = rbfs(grid, start_node, target_node)

print("Shortest path from", start_node, "to", target_node, ":", shortest_path)
