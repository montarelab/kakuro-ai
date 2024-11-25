from src.game_controller.algorithm import Algorithm
from src.parsing_validation.converters import graph_to_map
from src.parsing_validation.entities import Map


class FeedForward(Algorithm):
    _iteration = 0

    def __init__(self, game_map: Map) -> None:
        super().__init__(game_map)

    def solve(self) -> bool:
        """
        Solves the Kakuro puzzle using the FeedForward algorithm.
        """

        for node in self._blank_nodes:
            self._iteration += 1

            possible_values = list(node.get_possible_values(self._clues))
            length = len(possible_values)
            possible_values = reversed(possible_values)

            # If there is exactly one valid value, assign it
            if length >= 1:
                node.try_change_value(next(iter(possible_values)), self._clues)  # Assign the only value
                self._lambda(graph_to_map(self._map, self._blank_nodes))
            else:
                print('There is no solution. Feedforward algorithm failed.')
                # If more than one value is possible, this algorithm cannot proceed
                # without introducing backtracking.
                return False

        # If all nodes are filled and consistent, return True
        return all(node.value != 0 for node in self._blank_nodes)