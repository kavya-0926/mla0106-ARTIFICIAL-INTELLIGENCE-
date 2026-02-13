## Breadth First Search (BFS)
Algorithm BFS(Graph G, Start S)

1. Create empty Queue Q
2. Create empty VISITED list
3. Enqueue S into Q

4. While Q is not empty
       Remove front node N from Q
       If N not in VISITED
            Add N to VISITED
            Enqueue all neighbors of N
   End While

5. Print VISITED
End Algorithm

## Depth First Search (DFS)
Algorithm DFS(Graph G, Start S)

1. Create empty VISITED list

2. Define DFS(node)
       If node not in VISITED
            Add node to VISITED
            For each neighbor of node
                 Call DFS(neighbor)

3. Call DFS(S)

4. Print VISITED
End Algorithm

## Uniform Cost Search (UCS)
Algorithm UCS(Graph G, Start S)

1. Create Priority Queue PQ
2. Insert (0, S) into PQ
3. Create empty VISITED list

4. While PQ not empty
       Remove node with smallest cost
       If node not visited
            Add node to VISITED
            For each neighbor
                 Insert (cost + edge_cost, neighbor) into PQ
   End While

5. Print VISITED and total cost
End Algorithm

## Greedy Best First Search (GBFS)
Algorithm GBFS(Graph G, Start S, Goal G)

1. Create Priority Queue OPEN
2. Insert (h(S), S)
3. Create empty VISITED

4. While OPEN not empty
       Remove node with smallest h(n)
       If node = Goal
            Return path
       If node not visited
            Mark visited
            Insert all neighbors with h(n)
   End While

Return Failure
End Algorithm

## A* Search Algorithm
Algorithm A_STAR(Graph G, Start S, Goal G)

1. OPEN = Priority Queue
2. Insert (f(S)=h(S), S)
3. g(S) = 0
4. CLOSED = empty

5. While OPEN not empty
       Remove node N with smallest f(n)

       If N = Goal
            Return path

       Add N to CLOSED

       For each neighbor M
            new_g = g(N) + cost(N,M)

            If M not visited OR new_g < g(M)
                 g(M) = new_g
                 f(M) = g(M) + h(M)
                 parent[M] = N
                 Insert M into OPEN
   End While

Return Failure
End Algorithm

## Water Jug Problem (General BFS Method)
Algorithm WATER_JUG(Start_State, Goal_State)

1. Create Queue Q
2. Create VISITED set
3. Insert Start_State into Q

4. While Q not empty
       Remove current_state

       If current_state = Goal_State
            Return solution

       If not visited
            Mark visited
            Generate all possible pour states
            Add new states into Q
   End While

Return Failure
End Algorithm

## Min-Max Algorithm
Function MINIMAX(node, depth, isMax)

1. If node is leaf OR depth = 0
       Return node value

2. If isMax = TRUE
       best = -∞
       For each child
            best = max(best, MINIMAX(child, depth-1, FALSE))
       Return best

3. Else
       best = +∞
       For each child
            best = min(best, MINIMAX(child, depth-1, TRUE))
       Return best

## Alpha-Beta Pruning
Function ALPHABETA(node, depth, α, β, isMax)

1. If node is leaf OR depth = 0
       Return node value

2. If isMax = TRUE
       For each child
            α = max(α, ALPHABETA(child, depth-1, α, β, FALSE))
            If β ≤ α
                 Break   (Prune)
       Return α

3. Else
       For each child
            β = min(β, ALPHABETA(child, depth-1, α, β, TRUE))
            If β ≤ α
                 Break   (Prune)
       Return β
