from entities import Node, ClueNode



class Backtracking:
    iteration = 0

    def solve_kakuro_backtracking(self, blank_nodes: list[Node], clues: list[ClueNode]) -> bool:
        """
        Solves the Kakuro puzzle using the Backtracking algorithm.

        Args:
            blank_nodes: list of Node objects representing blank cells.
            clues: list of Clue objects representing row and column constraints.

        Returns:
            True if a solution is found, False otherwise.
        """

        def backtrack(index: int) -> bool:
            print('Backtracking iteration', self.iteration)
            self.iteration += 1
            """
            Recursive function to perform backtracking.
    
            Args:
                index: The index of the current node in the blank_nodes list.
    
            Returns:
                True if the puzzle can be solved, False if no solution exists.
            """
            if index == len(blank_nodes):  # Base case: All nodes are processed
                return True

            node = blank_nodes[index]
            possible_values = node.get_possible_values(clues)

            for value in possible_values:
                if node.try_change_value(value, clues):  # Check if assigning this value is valid
                    # Recursively process the next node
                    if backtrack(index + 1):
                        return True

                    # Undo assignment if the next steps fail
                    node.try_change_value(0, clues)
                    # node.value = 0
                    # if node.row is not None:
                    #     clues[node.row].update_sum()
                    # if node.column is not None:
                    #     clues[node.column].update_sum()

            return False  # No valid values, backtrack

        return backtrack(0)  # Start from the first node