import time
from src.game_controller.backtracking import Backtracking
from src.game_controller.dfs import Dfs
from src.game_controller.forward_checking import ForwardChecking
from src.parsing_validation.entities import Map
from src.parsing_validation.parse import parse_map
import matplotlib.pyplot as plt

maps = ['5x5_intermediate.json', '7x7_intermediate.json', '9x9_easy.json', '9x9_intermediate.json', '9x9_easy_unreal.json']
path = '../../maps/'

def ui_bind_mock(game_m: Map):
    pass

data = []

for current_map in maps:
    print('Map:', current_map)
    game_map = parse_map(path + current_map)

    # Backtracking
    start_time = time.time()
    backtracking = Backtracking(game_map)
    backtracking.bind(ui_bind_mock)
    b_result = backtracking.solve()
    b_iteration = backtracking.iteration
    b_time = time.time() - start_time  # Calculate elapsed time

    # DFS
    start_time = time.time()
    dfs = Dfs(game_map)
    dfs.bind(ui_bind_mock)
    d_result = dfs.solve()
    d_iteration = dfs.iteration
    d_time = time.time() - start_time  # Calculate elapsed time

    # Forward Checking
    start_time = time.time()
    fc = ForwardChecking(game_map)
    fc.bind(ui_bind_mock)
    f_result = fc.solve()
    f_iteration = fc.iteration
    f_time = time.time() - start_time  # Calculate elapsed time

    # Append statistics to data
    data.append({
        "map": current_map,
        "backtracking": {
            "iteration": b_iteration,
            "time": b_time
        },
        "dfs": {
            "iteration": d_iteration,
            "time": d_time
        },
        "forward_checking": {
            "iteration": f_iteration,
            "time": f_time
        }
    })

print(data)

# Extract data for plotting
maps = [entry['map'] for entry in data]
backtracking_iterations = [entry['backtracking']['iteration'] for entry in data]
dfs_iterations = [entry['dfs']['iteration'] for entry in data]
feedforward_iterations = [entry['forward_checking']['iteration'] for entry in data]

backtracking_times = [entry['backtracking']['time'] for entry in data]
dfs_times = [entry['dfs']['time'] for entry in data]
feedforward_times = [entry['forward_checking']['time'] for entry in data]

# Plotting Iterations
plt.figure(figsize=(10, 6))

plt.plot(maps, backtracking_iterations, marker='o', label='Backtracking', color='blue')
plt.plot(maps, dfs_iterations, marker='o', label='DFS', color='green')
plt.plot(maps, feedforward_iterations, marker='o', label='ForwardChecking', color='red')

# Adding labels and title for Iterations
plt.xlabel('Map', fontsize=12)
plt.ylabel('Number of Iterations', fontsize=12)
plt.title('Iterations per Algorithm for Different Maps', fontsize=14)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Plotting Execution Time
plt.figure(figsize=(10, 6))

plt.plot(maps, backtracking_times, marker='o', label='Backtracking Time', color='blue')
plt.plot(maps, dfs_times, marker='o', label='DFS Time', color='green')
plt.plot(maps, feedforward_times, marker='o', label='ForwardChecking Time', color='red')

# Adding labels and title for Time
plt.xlabel('Map', fontsize=12)
plt.ylabel('Execution Time (seconds)', fontsize=12)
plt.title('Execution Time per Algorithm for Different Maps', fontsize=14)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()