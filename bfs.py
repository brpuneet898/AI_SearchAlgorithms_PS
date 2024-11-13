# You are given an undirected graph represented as an adjacency list. You need to find the shortest path from a starting node to a target node in the graph using the BFS algorithm.

from collections import deque

# function to perform BFS and find the shortest path
def bfs(graph, start, target):
    # first check if the start and target are the same
    if start == target:
        return [start]
    
    # queue to manage nodes to visit (FIFO order)
    queue = deque([[start]])  # each item in the queue is a path
    # set to keep track of visited nodes
    visited = set([start])

    while queue:
        # get the current path from the queue
        current_path = queue.popleft()
        # get the last node in the current path
        current_node = current_path[-1]

        # check each neighbor of the current node
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                # create a new path by appending the neighbor to the current path
                new_path = list(current_path)  # copy the current path
                new_path.append(neighbor)
                
                # once you reached the target, return the new path
                if neighbor == target:
                    return new_path
                
                # else, add the new path to the queue and mark the neighbor as visited
                queue.append(new_path)
                visited.add(neighbor)
    
    # If no path is found or no solution exists, return an empty list
    return []

# Adjacency List
graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0, 3],
    3: [1, 2]
}

start_node = 0
target_node = 3
shortest_path = bfs(graph, start_node, target_node)

print("Shortest path from", start_node, "to", target_node, ":", shortest_path)