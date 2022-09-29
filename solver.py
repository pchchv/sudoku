from generator import *
import copy


Board = [
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

solbedBoard = copy.deepcopy(Board)


def sudokuSolver(board):
    # Get to the end of the board. The findEmpty function returns NONE
    find = findEmpty(board)
    if find is None:
        return True
    else:
        row, col = find
    for number in range(1, 10):
        if validator(board, number, (row, col)):
            board[row][col] = number
            if sudokuSolver(board):
                return True
            board[row][col] = 0
    return False


def mainSolver(level):
    sudokuGenerator(Board, level)
    solvedBoard = copy.deepcopy(Board)
    sudokuSolver(solvedBoard)
    return solvedBoard
