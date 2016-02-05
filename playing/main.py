import numpy as np
from numpy import *
from match import match

"""
Main file to play the game
"""

#file location of the trained model
#Eg: - 'C:\TicTacToe\playing\'
file_location = #location of model

if __name__ == '__main__' :
    print "Enter size of board"
    n = int(raw_input())
    
    #assign weight to the player here
    try:
        player = np.load(file_location+"model"+str(n)+".npy")
    except:
        print "Model not trained for "+str(n)+"*"+str(n)+" game"
        exit(1)

    print "Wanna start or go second ?"
    print "press 1 to start ... 2 to go second"
    preference = int(raw_input())
    
    match(player,preference)
