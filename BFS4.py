from collections import deque

n=int(input("Enter number of edges: "))
g={}

for _ in range(n):
    u,v=input("Enter edge (u v): ").split()
    g.setdefault(u,[]).append(v)
    g.setdefault(v,[])

start=input("Enter start node: ")

q=deque([start])
visited=[]

while q:
    node=q.popleft()
    if node not in visited:
        visited.append(node)
        q+=g[node]

print("BFS Traversal:")
print(" → ".join(visited))
