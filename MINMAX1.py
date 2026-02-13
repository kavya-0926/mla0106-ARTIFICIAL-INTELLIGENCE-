# Min-Max Algorithm

def minimax(depth, node_index, is_max, values, height):
    
    # If we reached leaf node
    if depth == height:
        return values[node_index]
    
    if is_max:
        return max(
            minimax(depth + 1, node_index * 2, False, values, height),
            minimax(depth + 1, node_index * 2 + 1, False, values, height)
        )
    else:
        return min(
            minimax(depth + 1, node_index * 2, True, values, height),
            minimax(depth + 1, node_index * 2 + 1, True, values, height)
        )


# Leaf node values (from your diagram example)
values = [10, 9, 14, 18, 5, 4, 50, 3]

import math
tree_height = math.log2(len(values))

result = minimax(0, 0, True, values, int(tree_height))

print("Optimal value:", result)
