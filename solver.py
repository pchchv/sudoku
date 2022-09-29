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

solbed_board = copy.deepcopy(Board)


def sudoku_solver(board):
    # Get to the end of the board. The findEmpty function returns NONE
    find = find_empty(board)
    if find is None:
        return True
    else:
        row, col = find
    for number in range(1, 10):
        if validator(board, number, (row, col)):
            board[row][col] = number
            if sudoku_solver(board):
                return True
            board[row][col] = 0
    return False


def main_solver(level):
    sudoku_generator(Board, level)
    solved_board = copy.deepcopy(Board)
    sudoku_solver(solved_board)
    return solved_board
