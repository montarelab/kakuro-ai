from backtracking import Backtracking
from data_structure import get_data_structure
from dfs import solve_kakuro_dfs
from entities import Game
from feedforward import solve_kakuro_feedforward
from parse import parse_map
from validation import validate_map

map_path = "../../maps/5x5_easy.json"

game = Game()

def evaluate() -> bool:
    for clue in game.clues:
        if not clue.is_valid():
            return False

    return True


def main():
    game.map = parse_map(map_path)
    validate_map(game.map)
    game.nodes, game.clues = get_data_structure(game.map)
    print('\nNodes were received:')

    print('DFS status:', solve_kakuro_dfs(game.nodes, game.clues))
    print('Backtracking status:', Backtracking().solve_kakuro_backtracking(game.nodes, game.clues))
    print('Feedforward status:', solve_kakuro_feedforward(game.nodes, game.clues))


if __name__ == "__main__":
    main()
