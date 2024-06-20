def check(board: list[list[int]]) -> bool:
    """Checks board and return True if board is allowed and False if not

    Args:
        board (list[list[int]]): List representation of board

    Returns:
        bool: Is board valid
    """
    cols = {i: set() for i in range(9)} 

    for row_index, row in enumerate(board):
        checked_in_row = set()
        for col_index, col in enumerate(row):
            value = board[row_index][col_index]
            if value != -1:
                if value in checked_in_row or value in cols[col_index]:
                    return False
                else:
                    checked_in_row.add(value)
                    cols[col_index].add(value)
    
    # Check Groups of 9
    for big_row in range(3):
        for big_col in range(3):
            checked: set = set()
            for row in range(big_row * 3, (big_row + 1) * 3):
                for col in range(big_col * 3, (big_col + 1) * 3):
                    number: int = board[row][col]
                    if number == -1:
                        pass
                    elif number in checked:
                        return False
                    else:
                        checked.add(number)
    # Return True
    return True