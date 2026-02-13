import heapq

def greedy_best_first_search(graph, heuristic, start, goal):
    open_list = []
    heapq.heappush(open_list, (heuristic[start], start))
    
    visited = set()
    parent = {start: None}
    
    while open_list:
        _, current = heapq.heappop(open_list)
        
        if current in visited:
            continue
        
        visited.add(current)
        
        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            return path[::-1]
        
        for neighbor in graph[current]:
            if neighbor not in visited:
                heapq.heappush(open_list, (heuristic[neighbor], neighbor))
                if neighbor not in parent:
                    parent[neighbor] = current
    
    return None


# -------- INPUT --------

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}

heuristic = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 1,
    'E': 4,
    'F': 3,
    'G': 0
}

start = 'A'
goal = 'G'

# -------- OUTPUT --------

path = greedy_best_first_search(graph, heuristic, start, goal)

if path:
    print("Path found:", " -> ".join(path))
else:
    print("No path found")
