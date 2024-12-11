from src.game_controller.algorithm import Algorithm
from src.parsing_validation.converters import graph_to_map
from src.parsing_validation.entities import Map, Node

# pros requires storing of only the current path, making it memory efficient, simple implementation, finds deep solution quickly
# cons sometimes limits on iterations can be made. kompletnost, nemusi najst najkratsiu cestu, v pripade vazeneho grafa zasekne lokalne minimumy

# pridavame indexy mozne hodnoty do stacku
# iterujeme indexy v cykluse, ak tam nebude hodnot, vratime sa spat do predosleho indexu


class Dfs(Algorithm):
    iteration = 0
    best_satisfied_condition = set()

    def __init__(self, game_map: Map) -> None:
        super().__init__(game_map)
        node =self._blank_nodes[-1]
        self.best_satisfied_condition = set()
        self.best_satisfied_condition.add((node.pos_x, node.pos_y))
        # self.best_satisfied_condition = [node.pos_y, node.pos_x]
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
            # All nodes processed successfully
            self._lambda(graph_to_map(self._map, self._blank_nodes))
            # print('Algo was successful')
            if self.is_game_solved():
                return True
            return False

        # iteration solver
        self.iteration += 1
        # if self.iteration >= 50000:
        #     print('Iterations have been exceeded')
        #     return False

        # init first node
        node = self._blank_nodes[current_index]
        possible_values = reversed(node.get_possible_values_dfs(self._clues))
        # traverse possible values (dfs)

        for value in possible_values:
            node.change_value_dfs(value)
            self._lambda(graph_to_map(self._map, self._blank_nodes))
            if self.dfs(current_index + 1):
                return True
                # Backtrack
            if not node.is_node_valid(self._clues):
                last_node_position = list(self.best_satisfied_condition)[-1]
                if node.pos_x < last_node_position[0] or node.pos_y < last_node_position[1]:
                    new_best_position = ()
                    if node.pos_x < last_node_position[0]:
                        new_best_position = (node.pos_x, last_node_position[1])
                    if node.pos_y < last_node_position[1]:
                        new_best_position = (node.pos_x, node.pos_y)

                    if not new_best_position in self.best_satisfied_condition:
                        self.best_satisfied_condition.add(new_best_position)
                        # self.best_satisfied_condition[1] = node.pos_x
                        # self.best_satisfied_condition[0] = node.pos_y
                        # print(f'Condition was satisfied for node ({new_best_position[0]} {new_best_position[1]})' )
                node.change_value_dfs(0)
                self._lambda(graph_to_map(self._map, self._blank_nodes))
            # else:
            #     print('node is not valid')
        # print(f'Backtracking on node index {current_index}')
        return False