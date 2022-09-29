import random


# firstBoard = [
#         [0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0]
#     ]


def board_printer(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:  # end of the row
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


def random_board_generator(board):
    # Getting to the end of the board - the function findEmpty return NONE
    find = find_empty(board)
    if find is None:  # if find != False
        return True
    else:
        row, col = find
    for number in range(1, 10):
        random_number = random.randint(1, 9) # TODO: The algorithm needs to be optimized
        if validator(board, random_number, (row, col)):
            board[row][col] = random_number
            if random_board_generator(board):
                return True
            board[row][col] = 0
    return False


def find_empty(board):
    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x] == 0:
                return y, x  # y = row , x = column
    # if we got here it mean that we finish the sudoku, so return none
    return None


def validator(board, number, coordinates):
    # checking row
    for x in range(len(board[0])):
        if number == board[coordinates[0]][x] and coordinates[1] != x:
            return False
    # checking column
    for y in range(len(board)):
        if number == board[y][coordinates[1]] and coordinates[0] != y:
            return False
    # checking the box
    box_x = coordinates[1] // 3
    box_y = coordinates[0] // 3
    for y in range(box_y * 3, box_y * 3 + 3):
        for x in range(box_x * 3, box_x * 3 + 3):
            if number == board[y][x] and (y, x) != coordinates:
                return False
    return True


def cells_deleter(board,number):
    while number:
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        if board[row][col] != 0:
            board[row][col] = 0
            number = number - 1


def sudoku_generator(board, level):
    random_board_generator(board)
    if level == 1:
        cells_deleter(board,30)
    if level == 2:
        cells_deleter(board,40)
    if level == 3:
        cells_deleter(board,50)
