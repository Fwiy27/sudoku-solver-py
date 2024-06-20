def get_coordinates(num: int) -> tuple[int, int]:
    """Get coordinates of row and col given board index 0-80

    Args:
        num (int): Board index 0-80

    Returns:
        tuple[int, int]: row, col
    """
    return int(num / 9), num % 9
        
def parse_line(input: str) -> list[int]:
    """Given string of numbers and other return valid line of board

    Args:
        input (str): String of numbers and other values

    Returns:
        list[int]: Valid board row
    """
    line = list()
    allowed_nums = list(range(1, 10))
    for i in range(9):
        try:
            num = input[i]
            line.append(int(num)) if int(num) in allowed_nums else line.append(-1)
        except:
            line.append(-1)
    return line

def request_lines() -> list[list[int]]:
    """Requests user to input lines of board and parses them

    Returns:
        list[list[int]]: Valid list representation of board
    """
    board = list()
    for i in range(1, 10):
        inp = input(f'Row {i}: ')
        board.append(parse_line(inp))
    return board