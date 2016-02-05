from math import *
from numpy import *

def sigmoid(z) :
    """
    z - matrix
    Returns:
        Sigmoid Function of z
    """
    return 1./(1+exp(-z))
