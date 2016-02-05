"""
N*N Tic Tac Toe Game

Player's Moves:
    1 - player1
    -1 - player2
    0 - empty box

n - Size of the board

"""



import operator
import numpy as np
from numpy import *
from random import random,randint,uniform
from sigmoid import sigmoid
from checkWin import checkWin
from checkComplete import checkComplete
from predict import predict

#game size(n*n)
n = 3

#players are nothing but the weights(it is a flattened vector)
def match(player,preference) :
    board = mat(zeros((n,n)))

    #empty boxes contain the boxes that are not filled yet
    empty_boxes = [x for x in range(n*n)]

    turnNo = 0
    while not checkWin(board) and not checkComplete(board) :
        turnNo += 1

        if preference == 2 and turnNo%2: #the computer starts the game and it's computer's move
            #the computer's move
            confidences = predict(player,board)
            confidences = [ (i,x) for i,x in enumerate(confidences)]
            confidences = sorted(confidences,key=operator.itemgetter(1),reverse=True)
            for i,confidence in confidences :
                if i in empty_boxes :
                    row = floor(i/n)
                    col = i%n
                    board[row,col] = 1
                    empty_boxes.remove(i)
                    break
        elif preference == 2 and not turnNo%2 :#the computer starts the game and it's user's move
            print "enter a number between 0-8 that is a legal move"
            box_no = int(raw_input())
            while box_no not in empty_boxes :
                print "enter a number between 0-8 that is a legal move"
                box_no = int(raw_input())
            row = floor(box_no/n)
            col = box_no%n
            board[row,col] = -1
            empty_boxes.remove(box_no)

        elif preference == 1 and turnNo%2: #the user starts the game and it's user's move
            print "enter a number between 0-8 that is a legal move"
            box_no = int(raw_input())
            while box_no not in empty_boxes :
                print "enter a number between 0-8 that is a legal move"
                box_no = int(raw_input())
            row = floor(box_no/n)
            col = box_no%n
            board[row,col] = 1
            empty_boxes.remove(box_no)

        else : #the user starts the game and it's computer's move
            #changing the board so as to make the player2 the current player
            pos = nonzero(board == 1)
            neg = nonzero(board == -1)
            board[pos] = -1
            board[neg] = 1
            confidences = predict(player,board)
            confidences = [ (i,x) for i,x in enumerate(confidences)]
            confidences = sorted(confidences,key=operator.itemgetter(1),reverse=True)
            for i,confidence in confidences :
                if i in empty_boxes :
                    row = floor(i/n)
                    col = i%n
                    board[row,col] = 1
                    empty_boxes.remove(i)
                    break
            pos = nonzero(board == 1)
            neg = nonzero(board == -1)
            board[pos] = -1
            board[neg] = 1
        print board

    #code to find the output of the game
    check_win = checkWin(board)

    if not check_win :  #draw
        print "draw"
    elif turnNo%2 :   #player1 has won
        if preference == 1 :
            print "user has won"
        else :
            print "computer has won"
    else :  #player2 has won
        if preference == 2 :
            print "user has won"
        else :
            print "computer has won"
            return 0

