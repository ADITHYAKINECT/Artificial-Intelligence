import random
import time
import copy

board =["_" for i in range(9)]
rows = 3
columns = 3  
players = ["O","X"]
available = list()
turn = None

def equal3(a,b,c):
    return a == b and b == c and a!= "_"

def isFull(board):
    # Returns true if the board is full
    return board.count("_") == 0

def isFree(board,pos):
    return board[pos] == "_"

def display(board):
    for i in range(rows):
        for j in range(columns):
            print(board[3 * i + j],end=" ")
        print("\n")
    print("*"*9)
    
def checkWinner(board):

    winner = None
    # check horizantal steak
    for i in range(rows):
        pos = 3*i
        if equal3(board[pos],board[pos+1],board[pos+2]):
            winner = board[pos]
    
    # check vertical steak
    for i in range(columns):
        if equal3(board[i],board[i+3],board[i+6]):
            winner = board[i]

    # check diagonal steaks
    if equal3(board[0],board[4],board[8]):
        winner = board[0]

    if equal3(board[2],board[4],board[6]):
        winner = board[2]
    
    if winner == None and isFull(board):
        winner = "Tie"
    
    return winner

def children(board):

    pos = list()
    for i in range(len(board)):
        if board[i] == "_":
            pos.append(i)
    return pos

def minimax(board,depth,maximizingPlayer):

    if depth == 0 or isFull(board) or checkWinner(board) is not None:
        if checkWinner(board) == players[0]:
            return 100000
        elif checkWinner(board) == players[1]:
            return -100000
        elif checkWinner(board) == "Tie":
            return 0

    if maximizingPlayer:
        value = -10000000000
        childpos = None
        for child in children(board):
            temp = copy.deepcopy(board)
            temp[child] = players[0]
            value_x = minimax(temp,depth-1,False) 
            if(value_x > value):
                value = value_x
                childpos = child
        return childpos

    else:
        value = 10000000000
        childpos = None
        for child in children(board):
            temp = copy.deepcopy(board)
            temp[child] = players[1]
            value_x = minimax(temp,depth-1,True)
            if(value_x < value):
                value = value_x
                childpos = child
        return childpos


def nextTurn(board,available,turn):
    if turn == 0:
        pos = minimax(board,5,True)

    else:
        while True:
            print("Available postions {}".format(available))
            pos = int(input("Enter the position: "))
            if pos in available:
                break
            else:
                print("Position {} is occupied".format(pos))
                continue
    available.remove(pos)
    board[pos] = players[turn]
    print("{}'s turn".format(players[turn]))
    display(board)

try:
    print("Press Control + C to terminate the Game")
    
    for i in range(len(board)):
        available.append(i)
    print(available)

    while turn not in [0,1]:
        turn = int(input("Press 1 to start game: "))
        if turn not in [0,1]:
            print("Please enter the valid number")
    while True:
        result = checkWinner(board)
        if result is not None:
            if result in players:
                print("and the Winner is {}".format(result))
            else:
                print("The game is Tie")
            break
        else:
            nextTurn(board,available,turn)
            turn = (turn + 1) % 2
            time.sleep(2)

except KeyboardInterrupt:
    print(" Game Interrupted :(")
