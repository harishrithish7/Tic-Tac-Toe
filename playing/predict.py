import numpy as np
from numpy import *
from sigmoid import sigmoid

def predict(theta,board) :
    """
    theta - unrolled Neural Network weights
    board - n*n matrix representing board
    Returns:
        h - n*1 column vector - confidence level for performing next move
    """
    n = size(board,1)

    #neural network parameters
    input_units = n*n
    hidden_units = n*n
    output_units = n*n

    #theta1 - unrolled weights between input and hidden layer
    #theta2 - unrolled weights between hidden and output layer
    theta1 = theta[:,:hidden_units*(input_units+1)]
    theta2 = theta[:,hidden_units*(input_units+1):]

    #reshaping to obtain rolled weights
    theta1 = np.reshape(theta1,(hidden_units,input_units+1))
    theta2 = np.reshape(theta2,(output_units,hidden_units+1))

    #calculating confidence level given board
    #position and neural network weights
    X = board.flatten().T
    X = concatenate((mat(1),X))
    z2 = theta1*X
    a2 = sigmoid(z2)
    a2 = concatenate((mat(1),a2))
    z3 = theta2*a2
    h = sigmoid(z3)
    return h
