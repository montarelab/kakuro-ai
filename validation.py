from parse import parse_map
from entities import Map, Cell
from errors import ValidationError


def validate_map(map: Map):
    if map.dimensions['rows'] * map.dimensions['columns'] != len(map.cells):
        raise ValidationError(f'Dimension is not apply to actual length of cells. Dimension {map.dimensions['rows']}x{map.dimensions['columns']}, but cells are {len(map.cells)}')
    
    if map.dimensions['rows'] <= 2 and map.dimensions['columns'] <= 2:
        raise ValidationError(f'Map size must be more than 2x2. Actual size is {map.dimensions['rows']}x{map.dimensions['columns']}')   

    for cell in map.cells:
        if cell.type != 'input' and cell.type != 'clue' and cell.type != 'block':
            raise ValidationError(f'Cell type must be input, clue or block. Actual type is {cell.type}')   

        if cell.type == 'clue':
            if cell.sumRow == None and cell.sumCol == None:
                raise ValidationError(f'In clue sum row or sum col must be defined')   

