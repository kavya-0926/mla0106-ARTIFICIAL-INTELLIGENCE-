from collections import deque

def water_jug_bfs(capacities, start, goal_amount):
    visited = set()
    queue = deque()
    queue.append((start, []))

    while queue:
        state, path = queue.popleft()

        if state in visited:
            continue

        visited.add(state)
        path = path + [state]

        # Check if any jug has the goal amount
        if goal_amount in state:
            return path

        # Generate next states
        for i in range(len(capacities)):
            for j in range(len(capacities)):
                if i != j:
                    new_state = list(state)

                    # Pour from jug i to jug j
                    pour_amount = min(state[i], capacities[j] - state[j])
                    new_state[i] -= pour_amount
                    new_state[j] += pour_amount

                    queue.append((tuple(new_state), path))

    return None


# -------- INPUT --------
capacities = (12, 8, 5)
start_state = (12, 0, 0)
goal = 6

# -------- OUTPUT --------
solution = water_jug_bfs(capacities, start_state, goal)

if solution:
    print("Steps to get 6 liters:")
    for step in solution:
        print(step)
else:
    print("No solution found")
