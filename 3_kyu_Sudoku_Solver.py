def sudoku(puzzle):
    row = 0
    col = 0
    while (sum(puzzle, [])).count(0) != 0:
        if puzzle[row][col] == 0:
            row_list = get_row(puzzle, row_index=row)
            col_list = get_col(puzzle, col_index=col)
            cube_list = get_cube(puzzle, row_index=row, col_index=col)
            unique_list = list(set(sum([row_list, col_list, cube_list], [])))
            range_list = list(range(10))
            dif_list = [item for item in range_list if item not in unique_list]
            if len(dif_list) == 1:
                for i in dif_list:
                    if i not in row_list and i not in col_list and i not in cube_list:
                        puzzle[row][col] = i
            res = set_coordinates(row, col)
            row = res[0]
            col = res[1]
        else:
            res = set_coordinates(row, col)
            row = res[0]
            col = res[1]

    return puzzle


def get_row(puzzle, row_index):
    return puzzle[row_index]


def get_col(puzzle, col_index):
    arr = []
    for i in range(9):
        arr.append(puzzle[i][col_index])
    return arr


def get_cube(puzzle, row_index, col_index):
    row = (row_index // 3) * 3
    col = (col_index // 3) * 3
    arr = []
    for i in range(3):
        arr.extend(puzzle[row + i][col:col + 3])
    return arr


def set_coordinates(row, col):
    if row == 8 and col == 8:
        col = 0
        row = 0
    elif col == 8:
        col = 0
        row += 1
    elif col < 8:
        col += 1
    return row, col
    
  
puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

sudoku(puzzle)

# Should return
 [[5,3,4,6,7,8,9,1,2],
  [6,7,2,1,9,5,3,4,8],
  [1,9,8,3,4,2,5,6,7],
  [8,5,9,7,6,1,4,2,3],
  [4,2,6,8,5,3,7,9,1],
  [7,1,3,9,2,4,8,5,6],
  [9,6,1,5,3,7,2,8,4],
  [2,8,7,4,1,9,6,3,5],
  [3,4,5,2,8,6,1,7,9]]
  
