import numpy as np
from numpy import *

def initialWeights(pop,gene_length) :
    """
    pop - popuation parameter of genetic algorithm
    gene_length - gene length of genetic algorithm
    Initial weights are generated using rand() function
    Returns:
        Matrix of size pop*gene_length
    """
    return [ mat(np.random.rand(1,gene_length)) for x in range(pop) ]
