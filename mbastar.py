# You are given a grid with cells that have a cost of moving through them. The goal is to find the shortest path from a starting point to a target point using the MBA* (Memory-Bounded A*) algorithm.

from heapq import heappop, heappush

# A helper function for calculating the Manhattan distance heuristic (h) between two points
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# Memory-Bounded A* algorithm
def mbastar(grid, start, target, memory_limit=10):
    # A helper function to perform the search with a given memory limit
    def search(node, g, path, memory):
        f = g + heuristic(node, target)  # Calculate f = g + h

        # If memory is full, prune the path (we limit the number of nodes stored in memory)
        if len(memory) > memory_limit:
            return float('inf')  # Return a large f value to prune this path

        if node == target:
            return path  # Found the target, return the path

        # Add the current node to memory
        memory.add(node)

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Possible moves: up, down, left, right
        
        # Explore neighbors
        for direction in directions:
            neighbor = (node[0] + direction[0], node[1] + direction[1])

            # Ensure the neighbor is within bounds of the grid
            if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]):
                # Skip already visited nodes in the current path or in memory
                if neighbor not in path and neighbor not in memory:
                    new_path = path + [neighbor]
                    result = search(neighbor, g + grid[neighbor[0]][neighbor[1]], new_path, memory)
                    if isinstance(result, list):  # If a valid path is returned
                        return result

        # If no valid path is found, return a high f value to prune this path
        return float('inf')

    # Start with an empty memory set
    memory = set()

    # Perform the search, starting with the initial node and heuristic as the limit
    result = search(start, 0, [start], memory)

    if isinstance(result, list):  # Found the path
        return result
    return []  # No solution found within memory limit

# Example grid (cost to move through each cell)
grid = [
    [1, 2, 1, 10],
    [1, 2, 1, 1],
    [1, 1, 1, 1],
    [10, 1, 1, 1]
]

start_node = (0, 0)  # Top-left corner
target_node = (3, 1)  # Bottom-right corner
memory_limit = 10  # Maximum memory limit for the search
shortest_path = mbastar(grid, start_node, target_node, memory_limit)

print("Shortest path from", start_node, "to", target_node, ":", shortest_path)
