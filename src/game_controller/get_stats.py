from src.game_controller.backtracking import Backtracking
from src.game_controller.dfs import Dfs
from src.game_controller.forward_checking import ForwardChecking
from src.parsing_validation.entities import Map
from src.parsing_validation.parse import parse_map

maps = ['5x5_intermediate.json', '7x7_intermediate.json', '9x9_easy.json', '10x12_intermediate.json', '9x9_easy_unreal.json']
path = '../../maps/'

def ui_bind_mock(game_m: Map):
    pass

data = []

for current_map in maps:
    print('Map:', current_map)
    game_map = parse_map(path + current_map)

    backtracking = Backtracking(game_map)
    backtracking.bind(ui_bind_mock)
    b_result = backtracking.solve()
    b_iteration = backtracking.iteration

    dfs = Dfs(game_map)
    dfs.bind(ui_bind_mock)
    d_result = dfs.solve()
    d_iteration = dfs.iteration

    fc = ForwardChecking(game_map)
    fc.bind(ui_bind_mock)
    f_result = fc.solve()
    f_iteration = fc.iteration

    data.append({
        "map": current_map,
        "backtracking": {
            "iteration": b_iteration
        },
        "dfs": {
            "iteration": d_iteration
        },
        "forward_checking": {
            "iteration": f_iteration
        }
    })

print(data)

import matplotlib.pyplot as plt
# Extract data for plotting
maps = [entry['map'] for entry in data]
backtracking_iterations = [entry['backtracking']['iteration'] for entry in data]
dfs_iterations = [entry['dfs']['iteration'] for entry in data]
feedforward_iterations = [entry['forward_checking']['iteration'] for entry in data]

# Plotting
plt.figure(figsize=(10, 6))

plt.plot(maps, backtracking_iterations, marker='o', label='Backtracking', color='blue')
plt.plot(maps, dfs_iterations, marker='o', label='DFS', color='green')
plt.plot(maps, feedforward_iterations, marker='o', label='ForwardChecking', color='red')

# Adding labels and title
plt.xlabel('Map', fontsize=12)
plt.ylabel('Number of Iterations', fontsize=12)
plt.title('Iterations per Algorithm for Different Maps', fontsize=14)
plt.legend()

# Show the plot
plt.grid(True)
plt.tight_layout()
plt.show()


