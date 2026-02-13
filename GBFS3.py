import heapq

def gbfs(graph, heuristic, start, goal):
    pq = []
    heapq.heappush(pq, (heuristic[start], start))
    visited = set()
    parent = {start: None}

    while pq:
        _, node = heapq.heappop(pq)

        if node in visited:
            continue

        visited.add(node)

        if node == goal:
            path = []
            while node:
                path.append(node)
                node = parent[node]
            return path[::-1]

        for neighbor in graph[node]:
            if neighbor not in visited:
                heapq.heappush(pq, (heuristic[neighbor], neighbor))
                if neighbor not in parent:
                    parent[neighbor] = node

    return None


# Graph (Right tree)
graph2 = {
    'P': ['A', 'C', 'R'],
    'A': [],
    'C': ['M', 'R', 'U'],
    'R': [],
    'M': [],
    'U': ['N', 'E'],
    'N': [],
    'E': []
}

# Heuristic values
heuristic2 = {
    'P': 0,
    'A': 11,
    'C': 6,
    'R': 8,
    'M': 9,
    'U': 4,
    'N': 0,
    'E': 5
}

start = 'P'
goal = 'N'

result = gbfs(graph2, heuristic2, start, goal)

print("Path:", result)
