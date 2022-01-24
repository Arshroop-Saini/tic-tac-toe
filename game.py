# TIC TAC TOE GAME

# Displaying the game board's UI
from IPython.display import clear_output

def display_board(board):
    print('\n'*100)  # Remember, this only works in jupyter!
    
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')



test_board = ['#','X','O','X','O','X','O','X','O','X']
display_board(test_board)



# Asking the user to choose a marker
def player_input():
    marker = ''
    
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


player_input()

# Asking the player to choose a position, Asking to choose where the user want to place his marker
# def answer():
#     choose_positions="hello world"
#     while choose_positions not in range(0,10):
#         choose_positions= int(input(" Please choose a position from 1-9: "))

#         if choose_positions not in range(0,10):
#             print("Please enterr a numberr between 1-9!")
#     return choose_positions

# # Taking in the positon and the marker as input and displaying the updated board
# answer()

def place_marker(board, marker, position):
    board[position] = marker

    


place_marker(test_board,'$',8)
display_board(test_board)

# Checking if someone has won the game or not
def win_check(board,mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal


win_check(test_board,'X')

# Choosing which player will go first
import random

def choose_first():
    player=random.randint(0,1)
    if player==0:
        return "Player 1"
    else:
        return "Player 2"





# Checking if the index position that we are selecting to place our marker is empty or not
def space_check(board, position):
    return board[position] == ""



# Checking if the board is empty or not, to check if the game is tried or not 
def full_board_check(board):
    for i in range(0,10):
        if space_check(board,i):
            return False
    return True

# Checking the input the user enters, checking if the position is in range, checking if the desired position is empty or not
def player_choice(board):
    position=0
    while position not in range[1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position=int(input("Please enter you next position (1-9): "))
    return position

# Asking the user if he/she want's to continue playing the game
def replay():
    
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

# Main GAME LOGIC, Brain of the game:
print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    
    play_game = input('Are you ready to play? Enter Yes or No.')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break





        
    
    
    





