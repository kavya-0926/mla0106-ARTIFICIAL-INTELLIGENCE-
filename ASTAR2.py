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


# ----- Graph (Top Figure) -----

graph1 = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('C', 2)],
    'C': [('E', 5)],
    'D': [('F', 2), ('G', 4)],
    'E': [('G', 3)],
    'F': [('G', 1)],
    'G': []
}

heuristic1 = {
    'A': 5,
    'B': 6,
    'C': 4,
    'D': 3,
    'E': 3,
    'F': 1,
    'G': 0
}

path, cost = a_star(graph1, heuristic1, 'A', 'G')

print("Path:", path)
print("Total Cost:", cost)
