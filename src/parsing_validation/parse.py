import json
import sys
from entities import Map, Block, Clue, Input


def parse_map(file_name: str):
    try:
        with open(file_name, 'r') as file:
            json_data = json.load(file)

            cells = []
            for cell in json_data['cells']:
                match cell['type']:
                    case 'block':
                        cells.append(Block())
                    case 'input':
                        cells.append(Input())
                    case 'clue':
                        cells.append(Clue(sumRow=cell['sumRow'], sumCol=cell['sumCol']))

            obj = Map(**json_data)
            obj.cells = cells
            print(f'Map was parsed  successfully! Map name: \'{file_name}\'')
            return obj
    except Exception as error:
        print('Error has been occured while reading file', file_name, 'with exception:\n', error)
        sys.exit(1)

# map = parse_map('maps/map1.json')
# cell = map.cells[4]
# print('test cell 5:', cell)
