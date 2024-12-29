# Mapping the logic
# Declare the board
# Print the board
# Current player = 'X'
# Loop
#   Ask the current player for a move
#   Store their mark on the board
#   Print the board
#   Check the winner
#   If we have a winner
#       Print a message
#       Break
#   If the board is full
#       Print a message
#       Break
#   Switch the current Player

# Solution
board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

def print_board(board):
    line = ('---+---+---')
    print(line)
    for row in board:
        print(f' {row[0]} | {row[1]} | {row[2]} ')
        print(line)

def check_winner(board):
    # Check rows
    for row in board: # row = ['X', 'X', 'X']
        if row[0] == row[1] == row[2] != ' ':
            return True
    # Check columns
    for col in range(3): # [0, 1, 2]
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return True
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != ' ' or \
       board[0][2] == board[1][1] == board[2][0] != ' ':
       return True
        
    return False

def is_full(board):
    for row in board:
        if ' ' in row:
            return False
    return True

def main():
    print_board(board)

    current_player = 'X'

    while True:
        print(f"Player {current_player}'s turn")
        row = int(input('Enter row (0-2): '))
        col = int(input('Enter col (0-2): '))

        if board[row][col] == ' ': # Check if the cell is empty
            board[row][col] = current_player
        else:
            print('This spot is already taken')
            continue

        print_board(board)

        if check_winner(board):
            print(f"Player {current_player} wins!")
            break   

        if is_full(board):
            print(f'The board is full!')
            break

        current_player = 'O' if current_player == 'X' else 'X'



if __name__ == '__main__':
    main()

    # def check_winner(board):
    #     # Check rows
    #     for row in board: # row = ['X', 'X', 'X']
    #         if row[0] == row[1] == row[2] == row[0] != ' ':
    #             return True
    #     # Check columns
    #     for col in range(3): # [0, 1, 2]
    #         if board[0][col] == board[1][col] == board[2][col] != ' ':
    #             return True
    #     # Check diagonals
    #     if board[0][0] == board[1][1] == board[2][2] != ' ' or \
    #        board[0][2] == board[1][1] == board[2][0] != ' ':
    #        return True
        
    #     return False
    

    # def check_full(board):
    #     for row in board:
    #         if ' ' in row:
    #             return False
            
    #     return True


    # def main():
    #     print_board(board)

    #     current_player = 'X'

    #     while True:
    #         print(f"Palyer {current_player}'s turn")
    #         row = int(input('Enter row (0-2): '))
    #         col = int(input('Enter col (0-2): '))

    #         if board[row][col] == ' ': # Check if the cell is empty
    #             board[row][col] = current_player
    #         else:
    #             print('This cell is already taken')
    #             continue

    #         print_board(board)

    #         if check_winner(board):
    #             print(f"Player {current_player} wins!")
    #             break

    #         if check_full(board):
    #             print(f'The board is full!')
    #             break

    #         # if current_player == 'X':
    #         #     current_player = 'O'
    #         # else:
    #         #     current_player = 'X'

    #         current_player = 'O' if current_player == 'X' else 'X'


    # if __name__ == '__main__':
    #     main()