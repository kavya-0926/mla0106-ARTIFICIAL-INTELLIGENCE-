from collections import deque

def water_jug_bfs(capacities, start, goal):
    visited = set()
    queue = deque()
    queue.append((start, []))

    while queue:
        state, path = queue.popleft()

        if state in visited:
            continue

        visited.add(state)
        path = path + [state]

        if state == goal:
            return path

        # Generate all possible pour actions
        for i in range(len(capacities)):
            for j in range(len(capacities)):
                if i != j:
                    new_state = list(state)
                    
                    pour = min(state[i], capacities[j] - state[j])
                    new_state[i] -= pour
                    new_state[j] += pour
                    
                    queue.append((tuple(new_state), path))

    return None


# ---- INPUT ----
capacities = (3, 5, 8)
start_state = (0, 0, 8)
goal_state = (0, 4, 4)

# ---- OUTPUT ----
solution = water_jug_bfs(capacities, start_state, goal_state)

if solution:
    print("Steps:")
    for step in solution:
        print(step)
else:
    print("No solution found")
