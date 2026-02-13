g = {}
n = int(input("Enter number of edges: "))

for _ in range(n):
    u, v = input("Enter edge (u v): ").split()
    g.setdefault(u, []).append(v)
    g.setdefault(v, [])

start = input("Enter start node: ")

visited = []

def dfs(node):
    if node not in visited:
        visited.append(node)
        for i in g[node]:
            dfs(i)

dfs(start)

print("DFS Traversal:")
print(" → ".join(visited))
