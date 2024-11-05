from entities import Map, Clue, Input, Block
from errors import ValidationError


def validate_map(map: Map):

    rows = map.dimensions['rows']
    cols = map.dimensions['columns']

    if rows * cols != len(map.cells):
        raise ValidationError(f'Dimension is not apply to actual length of cells. Dimension {rows}x{cols}, but cells are {len(map.cells)}')
    
    if rows <= 2 and cols <= 2:
        raise ValidationError(f'Map size must be more than 2x2. Actual size is {rows}x{cols}')   

    for cell in map.cells:
        if isinstance(cell, Clue):
            if cell.sumRow == None and cell.sumCol == None:
                raise ValidationError(f'In clue sum row or sum col must be defined')   
            
    print('Validation succeeded!')

