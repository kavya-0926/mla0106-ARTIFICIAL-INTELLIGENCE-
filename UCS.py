import heapq

g = {}
n = int(input("Enter number of edges: "))

for _ in range(n):
    u, v, w = input("Enter edge (u v cost): ").split()
    w = int(w)
    g.setdefault(u, []).append((v, w))
    g.setdefault(v, [])

start = input("Enter start node: ")

pq = [(0, start)]
visited = []
total_cost = 0

while pq:
    cost, node = heapq.heappop(pq)
    if node not in visited:
        visited.append(node)
        total_cost = cost
        for neigh, w in g[node]:
            heapq.heappush(pq, (cost + w, neigh))

print("UCS Traversal:")
print(" → ".join(visited))
print("Total Cost:", total_cost)
