from src.game_controller.algorithm import Algorithm
from src.parsing_validation.converters import graph_to_map
from src.parsing_validation.entities import Map


class Dfs(Algorithm):
    _iteration = 0

    def __init__(self, game_map: Map) -> None:
        super().__init__(game_map)

    def solve(self) -> bool:
        """
        Solves the Kakuro puzzle using Depth-First Search (DFS)
        """
        stack = []  # Stack to store (node index, current value) for backtracking
        current_index = 0
        while current_index < len(self._blank_nodes):

            print('DFS iteration: ', self._iteration)
            self._iteration += 1

            node = self._blank_nodes[current_index]

            # Initialize or continue processing the node
            if not stack or stack[-1][0] != current_index:
                l = list(node.get_possible_values(self._clues))
                possible_values = reversed(l)
                stack.append((current_index, iter(possible_values)))

            # Try the next value for the current node
            current_index, value_iterator = stack[-1]
            for value in value_iterator:
                if node.try_change_value(value, self._clues):
                    # Move to the next node
                    current_index += 1
                    self._lambda(graph_to_map(self._map, self._blank_nodes))
                    break
            else:
                # No valid value, backtrack
                stack.pop()
                if not stack:
                    print('There is no solution. DFS algorithm failed.')
                    self._lambda(graph_to_map(self._map, self._blank_nodes))
                    return False  # No solution
                current_index, _ = stack[-1]
                self._blank_nodes[current_index].try_change_value(0, self._clues)
                self._lambda(graph_to_map(self._map, self._blank_nodes))

        self._lambda(graph_to_map(self._map, self._blank_nodes))
        print('Algo was solved')
        return True