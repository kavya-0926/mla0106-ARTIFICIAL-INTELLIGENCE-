import math

def alphabeta(depth, node_index, alpha, beta, is_max, values, height):
    
    # If leaf node
    if depth == height:
        return values[node_index]
    
    # MAX Player
    if is_max:
        best = -math.inf
        
        for i in range(2):
            val = alphabeta(depth + 1,
                            node_index * 2 + i,
                            alpha, beta,
                            False, values, height)
            
            best = max(best, val)
            alpha = max(alpha, best)
            
            # Pruning condition
            if beta <= alpha:
                break
        
        return best
    
    # MIN Player
    else:
        best = math.inf
        
        for i in range(2):
            val = alphabeta(depth + 1,
                            node_index * 2 + i,
                            alpha, beta,
                            True, values, height)
            
            best = min(best, val)
            beta = min(beta, best)
            
            # Pruning condition
            if beta <= alpha:
                break
        
        return best


# Example leaf values (similar to your tree)
values = [2, 3, 5, 9, 0, 1, 7, 5]

tree_height = int(math.log2(len(values)))

result = alphabeta(0, 0, -math.inf, math.inf, True, values, tree_height)

print("Optimal value:", result)
