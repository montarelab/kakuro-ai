from entities import Map, Node, ClueNode

def solve_kakuro_dfs(blank_nodes: list[Node], clues: list[ClueNode]) -> bool:
    """
    Solves the Kakuro puzzle using Depth-First Search (DFS)
    """
    stack = []  # Stack to store (node index, current value) for backtracking
    current_index = 0
    iteration = 0

    while current_index < len(blank_nodes):

        print('DFS iteration: ', iteration)
        iteration += 1

        node = blank_nodes[current_index]

        # Initialize or continue processing the node
        if not stack or stack[-1][0] != current_index:
            possible_values = node.get_possible_values(clues)
            stack.append((current_index, iter(possible_values)))

        # Try the next value for the current node
        current_index, value_iterator = stack[-1]
        for value in value_iterator:
            if node.try_change_value(value, clues):
                # Move to the next node
                current_index += 1
                break
        else:
            # No valid value, backtrack
            stack.pop()
            if not stack:
                return False  # No solution
            current_index, _ = stack[-1]
            blank_nodes[current_index].try_change_value(0, clues)


    return True