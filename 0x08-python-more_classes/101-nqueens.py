#!/usr/bin/python3
"""Solving the N-Queens challenge problem.

The N queens puzzle is the challenge of placing
N non-attacking queens on an N×N chessboard.

Usage: ./101-nqueens.py <N>
    Where N must be an integer greater or equal to 4.

Returns: Every possible solution to the problem.
    One solution per line.
    Solutions are not printed in a specific order.
"""

from sys import argv


def printBoard(board):
    """Prints formated board
    Args:
        board (list): list of list of 0 or 1
    """
    board_vect = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                board_vect.append([i, j])
                break
    print(board_vect)


def valid_pos(board, row=0, col=0):
    """Check valid positions in col
    Args:
        row (int): row number of matrix
        col (int): colum number of matrix
    """
    for i in range(col):
        if board[row][i] == 1:
            return False
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1
    i = row
    j = col
    while j >= 0 and i < N:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1
    return True


def Solver(board, col=0):
    """Vefify the options
    Args:
        col (int): colum number of matrix
    """
    if col >= N:
        printBoard(board)
        return True
    res = False
    for i in range(N):
        if valid_pos(board, i, col):
            board[i][col] = 1
            res = Solver(board, col + 1) or res

            board[i][col] = 0
    return res


def n_queen():
    """Solves the N queens problem.
    Return: None
    """
    board = []
    for row in range(N):
        board.append([0] * N)
    if not Solver(board, 0):
        print("Not Solution Found")
        return
    return


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    if not argv[1].isdigit():
        print("N must be a number")
        exit(1)
    else:
        N = int(argv[1])

    if N < 4:
        print("N must be at least 4")
        exit(1)
    n_queen()
