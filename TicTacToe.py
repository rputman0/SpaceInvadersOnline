from random import *
'''Tic-Tac-Toe with two players'''

displayList = list("1|2|3\n4|5|6\n7|8|9")
board = list(" 123456789")

#return true if there is a digit in the string
def hasDigit(word):
    digits = " 12346789"
    for i in range(0,len(word)):
        if(word[i] == digits[i]):
            return True

def winningPos(first,second,third,pos):
    return board[first] == pos and board[second] == pos and board[third] == pos

#return true if the player wins
def isWin(pos):
    return ( winningPos(1,5,9,pos) or winningPos(3,5,7,pos) or
             winningPos(1,2,3,pos) or winningPos(4,5,6,pos) or
             winningPos(7,8,9,pos) or winningPos(1,4,7,pos) or
             winningPos(2,5,8,pos) or winningPos(3,6,9,pos) )

def assign(choice,letter):
    for i in range(0,len(board)):
        if(board[i] == choice):
            board[i] = letter

    for i in range(0,len(displayList)):
        if(choice == displayList[i]):
            displayList[i] = letter

print(''.join(displayList))

while(hasDigit("".join(board))):
    playerInput = input("Player 1(X): Choose a Position (1-9): ")
    assign(playerInput,"X")

    print(''.join(displayList))

    if(isWin("X")):
        print("You Win!")
        break

    opponnentInput = input("Player 2(O): Choose a Position (1-9): ")
    assign(opponnentInput,"O")

    print(''.join(displayList))

    if(isWin("O")):
        print("Player 2 Wins!")
        break
