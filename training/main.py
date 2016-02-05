"""
-> Code for training
-> Training is done with Neural Networks, the weights
   evolving over generations using genetic algorithm
-> 3 layer Feed Forward Neural Network
"""

import numpy as np
from numpy import *
from initialWeights import initialWeights
from match import match
from evolve import evolve

#file location to store the trained model
#Eg: - 'C:\TicTacToe\playing\'
file_location = #location of file
                 

#game size(n*n)
n = 3

#neural network parameters
input_units = n*n
hidden_units = n*n
output_units = n*n

#fitness parameters
#win1 - winning the match as player1
#win2 - winning the match as player2
#...
win1 = 1
win2 = 2
loss1 = -7
loss2 = -5
draw1 = 0
draw2 = 1

#genetic algorithm parameters
pop = 10
generations = 5
gene_length = hidden_units*(input_units+1) + output_units*(hidden_units+1)
       
if __name__ == '__main__':

    #initializing the players with random weights
    players = initialWeights(pop,gene_length)

    #playing each individual against each other,
    #with individuals evolving in each generation
    for gen in range(1,generations+1) :
        fitnesses = [0]*pop
        for i in range(pop) :
            for j in range(i+1,pop) :
                player1 = players[i]
                player2 = players[j]

                #first match
                curr_fitness = match(player1,player2,n,win1,\
                                     win2,loss1,loss2,draw1,draw2)
                fitnesses[i] += curr_fitness[0]
                fitnesses[j] += curr_fitness[1]
                
                #interchanging first and second player
                player1 = players[j]
                player2 = players[i]

                #second match
                curr_fitness = match(player1,player2,n,win1,\
                                     win2,loss1,loss2,draw1,draw2)
                fitnesses[j] += curr_fitness[0]
                fitnesses[i] += curr_fitness[1]

        players = evolve(players,fitnesses)

    #saving the best individual as the trained model
    np.save(file_location+str(n),players[0])


