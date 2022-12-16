import numpy as np

def valid_solution(board):
    # Rows
    for row in np.array(board):
        if np.sum(row) != 45:
            return False

    # Columns
    array = []
    for row in board:
        array.extend(row)
    for num in np.sum(np.array(array).reshape(len(board), len(board)), axis=0):
        if np.sum(num) != 45:
            return False

    # Cube3x3
    for row in range(1, len(board)-1, 3):
        for col in range(1, len(board[row]) - 1, 3):
            if np.sum(board[row-1][col - 1:col + 2]+board[row][col - 1:col + 2]+board[row + 1][col - 1:col + 2]) != 45:
                return False

    return True
  
  
validSolution([
  [5, 3, 4, 6, 7, 8, 9, 1, 2],
  [6, 7, 2, 1, 9, 5, 3, 4, 8],
  [1, 9, 8, 3, 4, 2, 5, 6, 7],
  [8, 5, 9, 7, 6, 1, 4, 2, 3],
  [4, 2, 6, 8, 5, 3, 7, 9, 1],
  [7, 1, 3, 9, 2, 4, 8, 5, 6],
  [9, 6, 1, 5, 3, 7, 2, 8, 4],
  [2, 8, 7, 4, 1, 9, 6, 3, 5],
  [3, 4, 5, 2, 8, 6, 1, 7, 9]
])
