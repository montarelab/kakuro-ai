from src.parsing_validation.entities import Node, ClueNode


def solve_kakuro_feedforward(blank_nodes: list[Node], clues: list[ClueNode]) -> bool:
    """
    Solves the Kakuro puzzle using the FeedForward algorithm.

    Args:
        blank_nodes: list of Node objects representing blank cells.
        clues: list of Clue objects representing row and column constraints.

    Returns:
        True if the puzzle is solved, False if it cannot be solved.
    """

    iteration = 0

    for node in blank_nodes:
        print('Feedforward iteration', iteration)
        iteration += 1

        possible_values = node.get_possible_values(clues)

        # If there is exactly one valid value, assign it
        if len(possible_values) == 1:

            node.try_change_value(next(iter(possible_values)), clues) # Assign the only value
            # node.value =
            # if node.row is not None:
            #     clues[node.row].update_sum()
            # if node.column is not None:
            #     clues[node.column].update_sum()
        elif len(possible_values) == 0:
            # No valid values for this node, inconsistent state
            return False
        else:
            # If more than one value is possible, this algorithm cannot proceed
            # without introducing backtracking.
            return False

    # If all nodes are filled and consistent, return True
    return all(node.value != 0 for node in blank_nodes)