from typing import List, Dict, TextIO
import random

blank = "-"
dim = 2
invalidMSG = "invalid input. Please try again: "
playerSymbol = "X"
oppSymbol = "O"
fileName = "moveset.txt"
record = False

def printBoard(board):
    for row in board:
        print(row[0] + "|" + row[1] + "|" + row[2])

def opponent(num,board,row,col):
    if num == 0:
        return easyBot(board)
    if num == 1:
        return medBot(board,row,col)
    if num == 2:
        return dataBot(board)
    if num == 3:
        return trainedBot(board)

def medBot(board,row,col):
    moveR, moveC = checkThreats(board,row,col)
    if moveR == -1:
        return randTile(board)
    return moveR, moveC

def dataBot(board,row,col): #redundant
    moveR, moveC = checkThreats(board,row,col)
    if moveR == -1:
        moveR, moveC = randTile(board)
    
    return moveR, moveC
    

def randTile(board):
    while True:
        row = random.randint(0,2)
        col = random.randint(0,2)
        if validSpot(board,row,col):
            return row, col

def checkThreats(board,row,col):
    def definedSpot(num):
        if num >= 0 and num <= dim:
            return True
    #going across row
    inRow = 0
    empty = -1
    for i in range(dim+1):
        coord = board[row][i]
        if coord == playerSymbol:
            inRow += 1
        elif coord == blank:
            empty = i  
    if inRow == 2 and empty != -1:
        print("a")
        return row,empty

    #going down column
    inRow = 0
    empty = -1
    for i in range(dim+1):
        coord = board[i][col]
        if coord == playerSymbol:
            inRow += 1
        elif coord == blank:
            empty = i
    if inRow == 2 and empty != -1:
        print("b")
        return empty,col

    #diagonal TL to BR
    inRow = 0
    empty = -1
    if row == col:
        for i in range(dim+1):
            coord = board[i][i]
            if coord == playerSymbol:
                inRow += 1
            elif coord == blank:
                empty = i
        if inRow == 2 and empty != -1:
            print("c")
            return empty,empty
            
    #diagonal TR to BL
    inRow = 0
    empty = -1
    if row == dim-col:
        for i in range(dim+1):
            coord = board[i][dim-i]
            if coord == playerSymbol:
                inRow += 1
            elif coord == blank:
                empty = i
        if inRow == 2 and empty != -1:
            return empty,dim-empty 
    return -1,-1


def getVal(prompt):
    while True:
        val = int (input(prompt))
        if val >= 0 and val <= 2:
            return val
        print("invalid input")

def easyBot(board):
    '''
        row = random.randint(0,2)
        col = random.randint(0,2)
        if validSpot(board,row,col):
            board[row][col] = oppSymbol
            break
    '''
    return randTile(board)


def validSpot(board,row,col):
    if row > dim or col > dim:
        return False
    if board[row][col] != blank:
        return False
    return True

def playerMove(board):
    while True:
        row = getVal("input row number: ")
        col = getVal("input column number: ")    
        if validSpot(board,row,col):
            break
        else:
            print(invalidMSG)
    board[row][col] = playerSymbol
    return row, col


def threeInRow(board,sign,row,col): #bugged
    if board[row][0] == board[row][1] and board[row][1] == board [row][2]:
        print("w")
        return True
    if board[0][col] == board[1][col] and board[1][col] == board[2][col]:
        print("x")
        return True
    if row == col :
        if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
            print("y")
            return True
    if row == 2-col: #or #(row == 2 and col == 2)
        if board[2][0] == board[1][1] and board[1][1] == board[0][2]:
            print("z")
            return True
        
    return False

def boardFull(board):
    for row in board:
        for tile in row:
            if row != blank:
                return False
    return True

while True:
    board = [[blank,blank,blank],[blank,blank,blank],[blank,blank,blank]]
    moves = ""
    while True: 


        row,col = playerMove(board)

        printBoard(board)
        moves = moves + str(row) + "," + str(col)               
        if threeInRow(board,"X",row,col):
            print("you win")
            moves = moves + ":L"
            break

        if boardFull(board):
            print("tie")
            moves = moves + ":T"
            break
        
        row1,col1 = opponent(1,board,row,col)
        print(row1,col1)
        moves = moves + ";" + str(row1) + "," + str(col1) + "|"
        board[row1][col1] = oppSymbol
            
        printBoard(board)

        if threeInRow(board,"O",row1,col1):
            print("you lose")
            moves = moves + ":W"
            break

    print(moves)
    if record:
        file = open(fileName,"w")
        file.write(moves)
        file.close
        

    q = input("press e to quit")
    if q == "e":
        break
