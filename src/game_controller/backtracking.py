from src.game_controller.algorithm import Algorithm
from src.parsing_validation.converters import graph_to_map
from src.parsing_validation.entities import Node, ClueNode, Map


class Backtracking(Algorithm):
    _iteration = 0

    def __init__(self, game_map: Map) -> None:
        super().__init__(game_map)

    def solve(self) -> bool:
        """
        Solves the Kakuro puzzle using the Backtracking algorithm.
        """
        def backtrack(index: int) -> bool:
            print('Backtracking iteration', self._iteration)
            self._iteration += 1
            """
            Recursive function to perform backtracking.
    
            Args:
                index: The index of the current node in the blank_nodes list.
    
            Returns:
                True if the puzzle can be solved, False if no solution exists.
            """
            if index == len(self._blank_nodes):  # Base case: All nodes are processed
                return True

            node = self._blank_nodes[index]
            possible_values = reversed(list(node.get_possible_values(self._clues)))

            for value in possible_values:
                if node.try_change_value(value, self._clues):  # Check if assigning this value is valid
                    self._lambda(graph_to_map(self._map, self._blank_nodes))

                    # Recursively process the next node
                    if backtrack(index + 1):
                        return True

                    # Undo assignment if the next steps fail
                    node.try_change_value(0, self._clues)
                    # node.value = 0
                    # if node.row is not None:
                    #     clues[node.row].update_sum()
                    # if node.column is not None:
                    #     clues[node.column].update_sum()

                self._lambda(graph_to_map(self._map, self._blank_nodes))
            return False  # No valid values, backtrack

        return backtrack(0)  # Start from the first node