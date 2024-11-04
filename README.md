# KakuroAI
An AI-powered solver for the Kakuro puzzle game, using Depth-First Search (DFS) and constraint-solving techniques to efficiently find solutions.

## Proposed tasks

- [ ] GUI
- [ ]  Preparation
    - [ ]  Find 5 maps: 4 of possible to solve + 1 impossible to solve
    - [ ]  Decide what text format to use
    - [ ]  Rewrite maps in corresponding text format
- [ ]  Developing
    - [ ]  Project structure
    - [ ]  Parsing functionality
    - [ ]  Validation functionality
    - [ ]  Data structure for cells
    - [ ]  Representing data in the correct format - graph
    - [ ]  DFS algorithm with backtracking and constraint propagation
    - [ ]  Evaluation functionality
- [ ]  Testing and metrics recordering
- [ ]  Presentation
    - [ ]  PDF documentation
    - [ ]  Video of working algo

## Project development

### Proposed idea for Data Structure

Node.

- Fields of Node:
    - value: int
    - row: NodeList
    - column: NodeList
    - right_node: Node
    - left_node: Node
    - upper_node: Node
    - bottom_node: Node
- Methods of Node:
    - change_value(val)

NodeList.

- Fields of NodeList:
    - sum_value: int # constant value defined on init
    - list_of_nodes: list<Node>()
    - remained_value: int # can be updated each time when a node in the list updates its value. Equals to sum_value - list_of_nodes.sum()
- Methods of NodeList:
    - get_available_values()
    - ccalculate_sum()

### Proposed data representation for an algo

- An array of nodes for traversing the graph via DFS
- A list of all NodeList's (all of the cols and rows) to simplify sum calculating in Evaluation stage

### Proposed method of data storage - JSON

```json
{
  "size": [7, 7],
  "sums": {
    "row": {"0,2": 23, "1,3": 24},
    "col": {"0,2": 16, "1,5": 17}
  },
  "empty_cells": ["0,0", "0,1", "0,3", "0,5"],
  // can be added for output: "filled_cells": {"0,5":"7", "3,7":"3"}
}
```

### Algorithms overview:

- DFS - for looking. In fact the whole game will be placed inside 1 recursive function which solves the game
- Backtracking - an ability which is remained by the using of DFS to come step or steps back when it’s required
- Constraint Propagation - check for the constraints before making a step

### Steps

1. Data Storage
2. Data Parsing
3. Data Validation (of input text files)
4. Game solving
5. Evaluation. During each step the game must be evaluated if all of the sums have been reached

## Describe an algorithm

### Step by step solution

Link on excalidraw: https://excalidraw.com/#json=poa1sLRgAiG8JW8sFMFnB,RsDsxRJbIlvSuNLg8nRgFg

 

<aside>
✅

Imagine the cells as nodes and the values (numbers) as paths. It’s the only one way how to make DFS algo for graphs applicable for our game

</aside>

- Algorithm moves left-to-right, up-to-bottom
- As the graph looks like a grid, so each node can be a neighbour with another 4. The order of adding nodes to the stack is the following:
    1. Right neighbour
    2. Upper neighbour
    3. Bottom neighbour
    4. Left neighbour
- Before assigning the value to the node, constraint functions checks what values are available
- Contraint functions are kind of functions which are executed before each step of the algorithm.
    - Their point is to predict the most appropriate assigning values to reduce the number of backtrackings in the future.
    - Constraint function finds suitable numbers analiticly without any AI
    - For example: Let’s imagine you have a column. Its sum needs to be 10, and it has 4 cells. So before the algo tries to put the number in the cell, it gets from a constraint function, that the only possible values are available for filling are 1,2,3, and 4! As only this combination of 4 unique digits more than 0 gets 10 in a sum.
- After validation algo tries to put the highest possible number
