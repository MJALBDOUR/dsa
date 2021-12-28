"""
    Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be
    validated according to the following rules:
        Each row must contain the digits 1-9 without repetition.
        Each column must contain the digits 1-9 without repetition.
        Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
    Note:
        A Sudoku board (partially filled) could be valid but is not necessarily solvable.
        Only the filled cells need to be validated according to the mentioned rules.
"""


def valid_sudoko(board):
    """Checking row, col then box"""
    return check_row(board) and check_col(board) and check_box(board)


def check_row(board):
    """Check duplicates in each row (short-cut)"""
    set_1 = set()
    for row in board:
        for num in row:
            if num != ".":
                if num not in set_1:
                    set_1.add(num)
                elif num in set_1:
                    return False
        set_1.clear()
    return True


def check_col(board):
    """Check duplicates in each col (short-cut)"""
    set_1 = set()
    for i in range(9):
        for j in range(9):
            num = board[j][i]
            if num != ".":
                if num not in set_1:
                    set_1.add(num)
                elif num in set_1:
                    return False
        set_1.clear()

    return True


def check_box(board):
    """Check duplicates in each box (short-cut)"""
    set_1 = set()
    for row in range(0, 9, 3):
        for col in range(0, 9, 3):
            set_1.clear()
            for i in range(3):
                for j in range(3):
                    num = board[i+row][j+col]
                    if num != ".":
                        if num not in set_1:
                            set_1.add(num)
                        elif num in set_1:
                            return False
    return True
