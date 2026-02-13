import heapq

def a_star(graph, heuristic, start, goal):
    open_list = []
    heapq.heappush(open_list, (heuristic[start], 0, start))
    
    g_cost = {start: 0}
    parent = {start: None}
    visited = set()

    while open_list:
        f, current_g, current = heapq.heappop(open_list)

        if current in visited:
            continue

        visited.add(current)

        if current == goal:
            path = []
            while current:
                path.append(current)
                current = parent[current]
            return path[::-1], g_cost[goal]

        for neighbor, cost in graph[current]:
            new_g = g_cost[current] + cost

            if neighbor not in g_cost or new_g < g_cost[neighbor]:
                g_cost[neighbor] = new_g
                f_value = new_g + heuristic[neighbor]
                heapq.heappush(open_list, (f_value, new_g, neighbor))
                parent[neighbor] = current

    return None, None


# -------- GRAPH (From Your Image) --------

graph = {
    'S': [('A', 3), ('D', 4)],
    'A': [('S', 3), ('B', 4), ('D', 5)],
    'B': [('A', 4), ('C', 4), ('E', 5)],
    'C': [('B', 4)],
    'D': [('S', 4), ('A', 5), ('E', 2)],
    'E': [('D', 2), ('B', 5), ('F', 4)],
    'F': [('E', 4), ('G', 3.5)],
    'G': [('F', 3.5)]
}

# -------- Heuristic Values h(n) --------

heuristic = {
    'S': 11.5,
    'A': 10.1,
    'B': 5.8,
    'C': 3.4,
    'D': 9.2,
    'E': 7.1,
    'F': 3.5,
    'G': 0
}

start = 'S'
goal = 'G'

path, cost = a_star(graph, heuristic, start, goal)

print("Path:", path)
print("Total Cost:", cost)
