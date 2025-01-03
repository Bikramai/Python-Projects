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

def get_position(prompt):
    while True:
        try:
            position = int(input(prompt))
            if position < 0 or position > 2:
                raise ValueError
            return position
        except ValueError:
            print('Invalid input!')
    

def get_move(current_player):
    print(f"Player {current_player}'s turn")
    while True:
        row = get_position('Enter row (0-2): ')
        col = get_position('Enter col (0-2): ')
        
        if board[row][col] == ' ': # Check if the cell is empty
            board[row][col] = current_player
            break

        print('This spot is already taken')
            


def main():
    print_board(board)

    current_player = 'X'

    while True:
        get_move(current_player)

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