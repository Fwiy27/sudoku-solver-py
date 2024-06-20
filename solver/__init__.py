import copy
from utils import get_coordinates
from checker import check

def solved(board: list[list[int]]) -> bool:
    """Return true if board is solved

    Args:
        board (list[list[int]]): List representation of board

    Returns:
        bool: _description_
    """
    return all(-1 not in row for row in board) and check(board)

def print_board(board: list[list[int]]) -> None:
    """Prints board

    Args:
        board (list[list[int]]): List representation of board
    """
    for row_index, row in enumerate(board):
        for col_index, number in enumerate(row):
            number = '-' if number == -1 else number
            print(f'[{number}]{" " if (col_index+1) % 3 == 0 else ""}', end = '')
        print( )
        print( ) if (row_index + 1) % 3 == 0 else None

def check_instance(board_index: int, value: int, board: list[list[int]], row_col = None) -> bool:
    """Check if value in board index would be valid

    Args:
        board_index (int): Board index 0-80
        value (int): Value for index 1-9
        board (list[list[int]]): List representation of board

    Returns:
        bool: If value in board would be valid
    """
    if not row_col:
        row, col = get_coordinates(board_index)
    else:
        row, col = row_col
        
    current_value = board[row][col]
    board[row][col] = value
    valid: bool = check(board)
    board[row][col] = current_value
    return valid

def get_available_values(board: list[list[int]], board_index: int, unavailable: dict[int, list]) -> list:
    """Get available values given board index

    Args:
        board (list[list[int]]): List representation of board
        board_index (int): Index of board 0-80
        unavailable (dict[int, list]): Dictionary of board indexes and their unavailable values (already checked and found they dont work)

    Returns:
        list: List of available values for board index
    """
    # Must be valid board
    # Must not be in unavailable
    row, col = get_coordinates(board_index)
    
    if board[row][col] != -1:
        return list()
    
    return [number for number in range(1, 10) if number not in unavailable[board_index] and check_instance(board_index, number, board, (row, col))]
    
def get_best_index_and_values(board: list[list[int]], unavailable: dict[int, list]) -> tuple[int, int]:
    """Get best index and available values for that index

    Args:
        board (list[list[int]]): List representation of board
        unavailable (dict[int, list]): Dictionary of board indexes and their unavailable values

    Returns:
        tuple[int, int]: Best index, unavailable values
    """
    all_indexes_and_values = dict()
    for index in range(81):
        row, col = get_coordinates(index)
        if board[row][col] == -1:
            all_indexes_and_values[index] = get_available_values(board, index, unavailable)

    min_index = min(all_indexes_and_values, key = lambda index: len(all_indexes_and_values[index]))

    min_index_value = -1 if len(all_indexes_and_values[min_index]) == 0 else min(all_indexes_and_values[min_index])

    return min_index, min_index_value

def solve(board: list[list[int]]) -> None:
    """Function to solve board in place

    Args:
        board (list[list[int]]): List representation of board
    """
    if not check(board):
        raise('Invalid Board')

    stack = list()
    unavailable: dict[int, list] = dict()
    for i in range(81):
        unavailable[i] = list()
    
    backing_up: bool = False

    while not solved(board):
        if not backing_up:
            current_index, set_value = get_best_index_and_values(board, unavailable)
            row, col = get_coordinates(current_index)
            if set_value == -1:
                backing_up = True
            else:
                stack.append(current_index)    
                board[row][col] = set_value
        else:
            current_index = stack.pop()
            row, col = get_coordinates(current_index)
            unavailable[current_index].append(board[row][col])
            board[row][col] = -1
            backing_up = False