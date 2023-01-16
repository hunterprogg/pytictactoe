# Tic Tac Toe in Python

won = False
currentPlayer = 1
board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
exohs = ['X', 'O']

# check if player is 0, if so return 1, otherwise return 0
def swap_player(player):
    if player == 0:
        return 1
    else: 
        return 0

# print out the board state in a grid, just like tic tac toe
def print_board(board):
    print("\n")
    for i  in range(len(board)):
        for j in range(len(board[i])):
            print(' ' + board[i][j], end='')
            if (j < len(board[i])-1):
                print(' |', end='')
        if (i < len(board)-1):
            print("\n-----------")
        else:
            print("\n")    

def position_to_indices(move):
    if move == 1:
        return (0,0)
    elif move == 2:
        return (0,1)
    elif move == 3:
        return (0,2)
    elif move == 4:
        return (1,0)
    elif move == 5:
        return (1,1)
    elif move == 6:
        return (1,2)
    elif move == 7:
        return (2,0)
    elif move == 8:
        return (2,1)
    elif move == 9:
        return (2,2)
    else:
        return (-1,-1)

def did_win(board, player):
    for row in board:
        if row[0] == row[1] and row[1] == row[2]:
            print("Player " + str(currentPlayer + 1) + " won!")
            return True
    
    for i in range(0, 3):
        if board[0][i] == board[1][i] and board[1][i] == board[2][i]:
            print("Player " + str(currentPlayer + 1) + " won!")
            return True

    if (board[0][0] == board[1][1] and board[1][1] == board[2][2]) or \
       (board[0][2] == board[1][1] and board[1][1] == board[2][0]):
        print("Player " + str(currentPlayer + 1) + " won!")
        return True

    return False

def process_move(board, index):
    if index[0] == -1:
        print("Invalid move!")
        raise ValueError()

    if board[index[0]][index[1]] == exohs[0] or board[index[0]][index[1]] == exohs[1]:
        print("Stop trying to cheat!")
        raise ValueError()

    board[index[0]][index[1]] = exohs[currentPlayer]

def no_legal_moves(board):
    for row in board:
        for cell in row:
            if cell != exohs[0] and cell != exohs[1]:
                return False
    return True

# Main loop
while (not won):
    currentPlayer = swap_player(currentPlayer)
    print_board(board)
    # Get player's move
    move = input("Player " + str(currentPlayer + 1) + " choose your cell: ")
    # Allow players to quit the game
    if move == 'q' or move == 'Q':
        break
    
    try:
        t = position_to_indices(int(move))
        # throw a ValueError if the move isn't legal
        process_move(board, t)
        won = did_win(board, currentPlayer)
        if won:
            print_board(board)
    except ValueError:
        currentPlayer = swap_player(currentPlayer)
        pass

    if no_legal_moves(board):
        print("Game is a draw!")
        break
    
