# You are given a grid with cells that have a cost of moving through them. The goal is to find the shortest path from a starting point to a target point using the A* algorithm.

from heapq import heappop, heappush

# Function to calculate the Manhattan distance heuristic (h) between two points
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# Function to perform A* search and find the shortest path
def astar(grid, start, target):
    # Create a priority queue to store nodes to visit, prioritized by f = g + h
    open_set = []
    heappush(open_set, (0 + heuristic(start, target), 0, start))  # (f, g, node)
    
    # Dictionary to store the cost of the path to each node (g value)
    g_costs = {start: 0}
    
    # Dictionary to store the parent of each node to reconstruct the path later
    came_from = {}
    
    # Directions for moving in the grid: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while open_set:
        # Get the node with the lowest f value from the priority queue
        _, g, current = heappop(open_set)

        # If we've reached the target, reconstruct and return the path
        if current == target:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path
        
        # Explore each neighbor
        for direction in directions:
            neighbor = (current[0] + direction[0], current[1] + direction[1])
            
            # Skip out-of-bounds neighbors
            if (0 <= neighbor[0] < len(grid)) and (0 <= neighbor[1] < len(grid[0])):
                # Calculate the tentative g score for the neighbor
                tentative_g = g + grid[neighbor[0]][neighbor[1]]
                
                # If the neighbor hasn't been visited or we've found a better path
                if neighbor not in g_costs or tentative_g < g_costs[neighbor]:
                    g_costs[neighbor] = tentative_g
                    f_score = tentative_g + heuristic(neighbor, target)
                    heappush(open_set, (f_score, tentative_g, neighbor))
                    came_from[neighbor] = current
    
    # If no path is found, return an empty list
    return []

# Example grid (cost to move through each cell)
grid = [
    [1, 2, 1, 10],
    [1, 2, 1, 1],
    [1, 1, 1, 1],
    [10, 1, 1, 1]
]

start_node = (0, 0)  # Top-left corner
target_node = (3, 3)  # Bottom-right corner
shortest_path = astar(grid, start_node, target_node)

print("Shortest path from", start_node, "to", target_node, ":", shortest_path)
