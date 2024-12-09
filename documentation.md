# Kakuro Solver Documentation

## Authors
Yurii Soma, Dmytro Tkachenko, Danylo Zahorulko

---

## 1. Task Definition

Kakuro is a logic puzzle that requires filling a grid with digits 1 through 9 such that the sum of digits in each row and column equals the value specified in adjacent triangular cells. Each number must be unique within its respective group (row or column sum). The task involves:

1. Implementing a software capable of solving Kakuro puzzles.
2. Reading initial puzzle configurations from json files.
3. Preparing at least five sample puzzles of varying difficulty (including one unsolvable case).
4. Solving puzzles using:
   - Depth-First Search (DFS),
   - Backtracking,
   - Forward Checking.
5. Demonstrating algorithm efficiency through statistical evaluation.
6. Delivering a video presentation of the results.

---

## 2. Problem Description

Kakuro puzzles are similar to crosswords but involve numbers instead of letters. The objective is to:
- Assign numbers to blank cells so that their sum matches the target value of the associated triangular cells.
- Ensure no digit repeats within a single group.

---

## 3. Algorithms to Test

### 3.1 Depth-First Search (DFS)

DFS traverses the search space by exploring each possible assignment of numbers to cells until a solution is found or the possibilities are exhausted.

**Mechanism:**
- Uses a stack-based approach (explicit or via recursion) to explore configurations.
- Backtracks when a constraint is violated.

**Limitations:**
- Inefficient for large or complex puzzles.
- May loop indefinitely without proper handling of cycles.


### 3.2 Backtracking

Backtracking is a systematic method for solving CSPs by exploring one possibility at a time and reverting changes when conflicts arise.

**Mechanism:**
- Assigns values to cells.
- Reverts (backtracks) when constraints are violated.

**Advantages:**
- Guarantees to find a solution (if it exists).

### 3.3 Forward Checking

Forward Checking improves backtracking by preemptively eliminating invalid values from consideration for future variables based on current assignments.

**Mechanism:**
- Updates domains of unassigned cells after each assignment.
- Backtracks when a domain becomes empty.

**Advantages:**
- Reduces the search space significantly.

---

## 4. Evaluation

To demonstrate the efficiency of the algorithms, the following metrics will be recorded:
1. **Average Execution Time**
2. **Number of States Explored**

### Statistical Comparisons
Results for puzzles of varying difficulty levels will be presented in a table, comparing the algorithms' performance.

| Puzzle | Algorithm         | Solutions Found | Avg. Time (ms) | 
|--------|-------------------|-----------------|----------------|
| 1      | DFS               | x/x             | xxx            | 
| 1      | Backtracking      | x/x             | xxx            | 
| 1      | Forward Checking  | x/x             | xxx            | 
