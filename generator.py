import random


firstBoard = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

def randomBoardGenerator(board):
    # Getting to the end of the board - the function findEmpty return NONE
    find = findEmpty(board)
    if find is None:  # if find != False
        return True
    else:
        row, col = find
    for number in range(1, 10):
        randomNumber = random.randint(1, 9) # TODO: The algorithm needs to be optimized
        if validator(board, randomNumber, (row, col)):
            board[row][col] = randomNumber
            if randomBoardGenerator(board):
                return True
            board[row][col] = 0
    return False

def findEmpty(board):
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

def sudokuGenerator(firstBoard, level):
    randomBoardGenerator(firstBoard)