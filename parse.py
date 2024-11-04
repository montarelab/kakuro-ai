import json
import sys
from entities import Map, Cell

def parse_map(file_name: str):
    try:
        with open(file_name, 'r') as file:
            json_data = json.load(file)
            cells = [Cell(**cell) for cell in json_data['cells']]
            obj = Map(**json_data)
            obj.cells = cells
            return obj
    except Exception as error:
        print('Error has been occured while reading file', file_name, 'with exception:\n', error)
        sys.exit(1)



map = parse_map('maps/map1.json')
cell = map.cells[4]
print('test cell 5:', cell)