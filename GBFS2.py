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


# Graph (Left figure)
graph1 = {
    'P': ['R', 'C', 'A'],
    'R': ['C', 'S'],
    'C': ['U'],
    'A': ['M'],
    'M': ['L'],
    'L': ['N'],
    'U': ['S', 'N'],
    'N': [],
    'S': []
}

# Heuristic values
heuristic1 = {
    'P': 10,
    'R': 8,
    'C': 6,
    'A': 11,
    'M': 9,
    'L': 9,
    'U': 4,
    'N': 0,
    'S': 0
}

start = 'P'
goal = 'S'

result = gbfs(graph1, heuristic1, start, goal)

print("Path:", result)
