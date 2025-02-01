from src.game_controller.algorithm import Algorithm
from src.parsing_validation.converters import graph_to_map
from src.parsing_validation.entities import Map, Node
from time import  sleep

class Dfs(Algorithm):
    iteration = 0
    best_satisfied_condition = set()

    def __init__(self, game_map: Map) -> None:
        super().__init__(game_map)
        node =self._blank_nodes[-1]
        self.best_satisfied_condition = set()
        self.best_satisfied_condition.add((node.pos_x, node.pos_y))
        print(f'Condition was satisfied for node ({self.best_satisfied_condition})')

    def is_game_solved(self):
        for clue in self._clues:
            if not clue.is_valid():
                return False
        return True

    def solve(self) -> bool:
        if self.dfs(0):
            print('Dfs Algo was solved')
            return True
        print('Dfs Algo was failed')
        return False

    def dfs(self, current_index=0):
        """
        Solves the Kakuro puzzle using recursive Depth-First Search (DFS).
        :param current_index: The current index of the node being processed.
        """
        # validation
        if current_index >= len(self._blank_nodes):
            if self.is_game_solved():
                return True
            return False

        self.iteration += 1

        # init first node
        node = self._blank_nodes[current_index]
        possible_values = reversed(node.get_possible_values_dfs(self._clues))

        for value in possible_values:
            node.change_value_dfs(value)

            sleep(0.0)
            self._lambda(graph_to_map(self._map, self._blank_nodes))

            if self.dfs(current_index + 1):
                return True
                # Backtrack

            if not node.is_node_valid(self._clues):

                node.change_value_dfs(0)

        return False