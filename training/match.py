import operator
from numpy import *
from predict import predict
from checkWin import checkWin
from checkComplete import checkComplete

def match(player1,player2,n,win1,win2,loss1,loss2,draw1,draw2) :
    """
    The function is used to play a game between player1 and player2

    player1,player2 - vector containing the weights associated with the player
    n - size of  the board
    Fitness parameters:
        win1 - winning the match as player1
        win2 - winning the match as player2
        ...
        
    Returns:
        Fitness parameter for player1 and player2 which depends on result of the game played
    """
    
    board = mat(zeros((n,n)))

    #empty boxes - boxes that have not been used by either of the players
    empty_boxes = [x for x in range(n*n)]

    turnNo = 0
    while not checkWin(board) and not checkComplete(board) :
        turnNo += 1
        if turnNo%2 :
            #choosing the move that has the highest confidence
            #among those that haven't been played yet
            confidences = predict(player1,board)
            confidences = [ (i,x) for i,x in enumerate(confidences)]
            confidences = sorted(confidences,key=operator.itemgetter(1),reverse=True)
            for i,confidence in confidences :
                if i in empty_boxes :
                    row = floor(i/n)
                    col = i%n
                    board[row,col] = 1
                    empty_boxes.remove(i)
                    break

        else :
            #changing the board so as to make the player2 the current player
            pos = nonzero(board == 1)
            neg = nonzero(board == -1)
            board[pos] = -1
            board[neg] = 1

            #choosing the move that has the highest confidence
            #among those that haven't been played yet
            confidences = predict(player2,board)
            confidences = [ (i,x) for i,x in enumerate(confidences)]
            confidences = sorted(confidences,key=operator.itemgetter(1),reverse=True)
            for i,confidence in confidences :
                if i in empty_boxes :
                    row = floor(i/n)
                    col = i%n
                    board[row,col] = 1
                    empty_boxes.remove(i)
                    break

            #inveritng the board so as to make player1 the current player
            pos = nonzero(board == 1)
            neg = nonzero(board == -1)
            board[pos] = -1
            board[neg] = 1

    #code to return the fitness of player1 and player2
    check_win = checkWin(board)

    if not check_win :  #draw
        return (draw1,draw2)
    elif turnNo%2 :   #player1 has won
        return (win1,loss2)
    else :  #player2 has won
        return (loss1,win2)
