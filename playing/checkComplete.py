"""Returns:
    1 - board is complete
    0 - board is incomplete
"""

def checkComplete(board) :
    for row in board :
        if 0 in row :
            return 0
    return 1
