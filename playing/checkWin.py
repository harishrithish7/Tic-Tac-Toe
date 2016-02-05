"""Returns:
    1 - player_1 has won
    -1 - player_2 has won
    0 - no one has won yet
"""

import numpy as np
from numpy import *

def checkWin(board) :
    n = size(board,1)
    #checking for horizontal vertical and diagonal winning conditions
    if n in np.sum(board,0) or n in np.sum(board,1) or n == np.trace(board,0) or n == np.trace(np.fliplr(board)) :
        return 1
    elif -n in np.sum(board,0) or -n in np.sum(board,1) or -n == np.trace(board,0) or -n == np.trace(np.fliplr(board)) :
        return -1
    return 0 
