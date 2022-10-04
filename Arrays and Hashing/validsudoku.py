# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells 
# need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the 
# digits 1-9 without repetition.

# Note:
# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned

import collections

def validSudoku(board):
     # collections.defaultdict is a subclass of dict that doesn't throw 
     # key errors, rather creates a key with given value
    row = collections.defaultdict(set) 
    # row = {i: set() for i in range(9)} also works for row and col or 
    # row = {1: set(), 2: set(), 3: set(), 4: set(), 5: set(), 6: set(), 
    # 7: set(), 8: set(), 9: set()} also works (bruteforce method)
    col = collections.defaultdict(set)
    # Since box takes key as a tuple, the second method doesn't work
    box = collections.defaultdict(set)

    for r in range(9):
        for c in range(9):
            if board[r][c] == '.':
                continue
            if ((board[r][c] in row[r]) or (board[r][c] in col[c]) or
            (board[r][c] in box[(r//3, c//3)])):
                return False
            row[r].add(board[r][c])
            col[c].add(board[r][c])
            box[(r//3, c//3)].add(board[r][c])
        return True