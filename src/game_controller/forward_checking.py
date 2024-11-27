from src.game_controller.algorithm import Algorithm
from src.parsing_validation.converters import graph_to_map
from src.parsing_validation.entities import Node, ClueNode, Map


class ForwardChecking(Algorithm):
    iteration = 0

    def __init__(self, game_map: Map) -> None:
        super().__init__(game_map)

    def solve(self) -> bool:
        """
        Solves the Kakuro puzzle using the Forward Checking algorithm.
        """

        def forward_check(node: Node, value: int) -> bool:
            """
            Assigns a value to a node and propagates constraints to check consistency.
            """

            # Update constraints for the row and column
            node.try_change_value(value, self._clues)

            # Check if the assignment causes any conflicts
            for n in self._blank_nodes:
                self.iteration += 1

                if n.value == 0:  # Only consider unassigned nodes
                    possible_values = n.get_possible_values(self._clues)
                    if not possible_values:  # If no values are possible, conflict detected
                        return False
            return True

        def backtrack(index: int) -> bool:
            """
            Recursively assigns values to nodes using Forward Checking.
            """
            if index == len(self._blank_nodes):  # Base case: all nodes are assigned
                return True

            node = self._blank_nodes[index]
            valid_values = node.get_possible_values(self._clues)

            valid_values = reversed(list(valid_values))

            for value in valid_values:

                if forward_check(node, value):  # Assign value and check constraints
                    self.iteration += 1

                    if self.iteration >= 1000:
                        print('Iterations have been exceed')
                        return False

                    self._lambda(graph_to_map(self._map, self._blank_nodes))

                    if backtrack(index + 1):  # Recurse to the next node
                        return True
                # Undo assignment if it leads to failure

                node.try_change_value(0, self._clues)

            return False

        backtrack(0)
        if self.is_succeed():
            return True
        print('Forward checking Algorithm failed')
        return False