
import random

board = [' '] * 10#list
symbol=input("you can choose your symbol \n X\n O")
symbol=symbol.upper()

if symbol=="X":
    computer="O"
    human="X"
else:
    computer="X"
    human="O"

print("computer selected ",computer)
print("you selected ",human)

#using for displaying board
def display_board(board):
    print(board[1]+"___|___"+board[2]+"___|___"+board[3])
    print(board[4]+"___|___"+board[5]+"___|___"+board[6])
    print(board[7]+"   |   "+board[8]+"   |   "+board[9])
    print('-' * 20,'\n')


def check_win():
    if board[1] == board[2] == board[3] and board[1] != ' ':
        return True
    elif board[4] == board[5] == board[6] and board[4] != ' ':
        return True
    elif board[7] == board[8] == board[9] and board[7] != ' ':
        return True
    elif board[1] == board[4] == board[7] and board[1] != ' ':
        return True
    elif board[2] == board[5] == board[8] and board[2] != ' ':
        return True
    elif board[3] == board[6] == board[9] and board[3] != ' ':
        return True
    elif board[1] == board[5] == board[9] and board[1] != ' ':
        return True
    elif board[7] == board[5] == board[3] and board[7] != ' ':
        return True
    else:
        return False


def check_draw():
    if board.count(' ') < 2:
        return True
    else:
        return False

#using for checking a position is already taken or not
def is_available(pos):
    #return True if board[pos] == ' ' else False
    if board[pos] == ' ':
        return True
    else:
        return False

def insert(letter, pos):
    if is_available(pos):
        board[pos] = letter
        display_board(board)
        if check_win():
            if letter == computer:
                print("Computer Wins")
                exit()
            else:
                print("Human wins")
                exit()
        if check_draw():
            print("Draw")
            exit()
    else:
        if letter == human:
            pos = int(input("Not Free! Please re-enter a position"))
        else:
            pos = random.randint(1, 9)
            print("computer selected the position ",pos)
        insert(letter, pos)


def human_move(letter):
    pos = int(input("Enter the position to insert:"))
    insert(letter, pos)


def computer_move(letter):
    pos = random.randint(1, 9)
    print("computer selected the position ",pos)
    insert(letter, pos)


# main loop
display_board(board)
while not check_win():
    computer_move(computer)
    human_move(human)


#make the board
#write the checking conditions
#create a function for checking availabaility of positions
#create a function to check draw
#create function for computer
#create a function for player
#create insert function

