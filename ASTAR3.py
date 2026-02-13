import heapq

def a_star(graph, heuristic, start, goal):
    pq = []
    heapq.heappush(pq, (heuristic[start], 0, start))

    g_cost = {start: 0}
    parent = {start: None}

    while pq:
        f, g, node = heapq.heappop(pq)

        if node == goal:
            path = []
            while node:
                path.append(node)
                node = parent[node]
            return path[::-1], g_cost[goal]

        for neighbor, cost in graph[node]:
            new_g = g_cost[node] + cost

            if neighbor not in g_cost or new_g < g_cost[neighbor]:
                g_cost[neighbor] = new_g
                f_value = new_g + heuristic[neighbor]
                heapq.heappush(pq, (f_value, new_g, neighbor))
                parent[neighbor] = node

    return None, None


# ----- Graph (Bottom Figure) -----

graph2 = {
    'S': [('A', 4), ('D', 2)],
    'A': [('B', 5), ('C', 10)],
    'B': [('C', 2), ('E', 1), ('D', 1)],
    'C': [('G', 4)],
    'D': [('E', 4)],
    'E': [('G', 3)],
    'G': []
}

# (Heuristic assumed from diagram style — adjust if needed)
heuristic2 = {
    'S': 7,
    'A': 4,
    'B': 4,
    'C': 2,
    'D': 5,
    'E': 3,
    'G': 0
}

path, cost = a_star(graph2, heuristic2, 'S', 'G')

print("Path:", path)
print("Total Cost:", cost)
