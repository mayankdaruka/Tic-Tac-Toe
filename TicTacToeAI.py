
playing_game = True
         
def display_board(board):
    """ Displays the tic-tac-toe board """
    print('         |         |')
    print('    ' + board[0] + '    |    ' + board[1] + '    |    ' + board[2])
    print('         |         |')
    print('-----------------------------')
    print('         |         |')
    print('    ' + board[3] + '    |    ' + board[4] + '    |    ' + board[5])
    print('         |         |')
    print('-----------------------------')
    print('         |         |')
    print('    ' + board[6] + '    |    ' + board[7] + '    |    ' + board[8])
    print('         |         |')
    print('                             ')
    print('#############################')
    print('                             ')
    
def check_win(board,player_marker):
    """ Checks if computer/player wins """
    return ((board[0] == player_marker and board[1] == player_marker and board[2] == player_marker) or 
            (board[3] == player_marker and board[4] == player_marker and board[5] == player_marker) or
            (board[6] == player_marker and board[7] == player_marker and board[8] == player_marker) or
            (board[0] == player_marker and board[3] == player_marker and board[6] == player_marker) or
            (board[1] == player_marker and board[4] == player_marker and board[7] == player_marker) or
            (board[2] == player_marker and board[5] == player_marker and board[8] == player_marker) or
            (board[0] == player_marker and board[4] == player_marker and board[8] == player_marker) or
            (board[2] == player_marker and board[4] == player_marker and board[6] == player_marker))
            
def check_draw(board):
    """ Checks for a draw """
    return ' ' not in board

def get_duplicate_board(board):
    """ Makes a duplicate of the board so that we can test moves without
        changing the actual board """
    duplicate = []
    for part in board:
        duplicate.append(part)
    return duplicate

def test_win(board,mark,square):
    """ Allows computer to test each move on the duplicate board """
    duplicate = get_duplicate_board(board)
    duplicate[square] = mark
    return check_win(duplicate,mark)

def test_fork(board,mark,square):
    """ Determines if a move opens up a fork """  
    duplicate = get_duplicate_board(board)
    duplicate[square] = mark
    num_wins = 0
    for num in range(9):
        if(duplicate[num] == ' ' and test_win(duplicate,mark,num)):
            num_wins += 1
    return num_wins >= 2  

def get_computer_move(board):
    """ Allows computer to check and consider all moves to make a decision"""
    #Checks for moves in which the computer can win
    for square in range(9):
        if(board[square] == ' ' and test_win(board,'X',square)):
            return square
    #Checks for moves in which the player can win
    for square in range(9):
        if(board[square] == ' ' and test_win(board,'O',square)):
            return square
    #Checks fork opportunities for the computer
    for square in range(9):
        if(board[square] == ' ' and test_fork(board,'X',square)):
            return square
    #Checks fork opportunities for the player (including two forks)
    num_forks = 0
    for square in range(9):
        if(board[square] == ' ' and test_fork(board,'O',square)):
            num_forks += 1
            temp_move = square
    if num_forks == 1:
        return temp_move
    elif num_forks == 2:
        for index in [1,3,5,7]:
            if board[index] == ' ':
                return index
    #Plays center if empty
    if board[4] == ' ':
        return 4
    #Plays a corner if empty
    for index in [0,2,6,8]:
        if board[index] == ' ':
            return index
    #Plays a side
    for index in [1,3,5,7]:
        if board[index] == ' ':
            return index
    

while playing_game:
    in_game = True
    board = [' ']*9
    input1 = input("Would you like to go first(1) or second(2)? ")
    if input1 == 1:
        player_marker = 'O'
    else:
        player_marker = 'X'
    display_board(board)
    while in_game:
        if player_marker == 'O':
            move = int(input("Player Go - Index(0-8)"))
            if board[move] != ' ':
                print "Invalid move! Choose an empty square!"
                continue
        else:
            move = get_computer_move(board)
        board[move] = player_marker
        if check_win(board,player_marker):
            in_game = False
            display_board(board)
            if player_marker == 'O':
                print "The Player wins!"
            else:
                print "The Computer wins!"
            continue      
        if check_draw(board):
            in_game = False
            display_board(board)
            print "It's a draw!"
            continue
        display_board(board)
        if player_marker == 'O':
            player_marker = 'X'
        else:
            player_marker = 'O'
    input2 = input("Type Y/y to keep playing!")
    if (input2 != 'Y') or (input2 != 'y'):
        playing_game = False
  
