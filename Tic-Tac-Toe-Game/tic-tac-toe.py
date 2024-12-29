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

    current_player = 'X'

    while True:
        print(f"Palyer {current_player}'s turn")
        row = int(input('Enter row (0-2): '))
        col = int(input('Enter col (0-2): '))

        if board[row][col] == ' ': # Check if the cell is empty
            board[row][col] = current_player
        else:
            print('This cell is already taken')
            continue

        print_board(board)

print_board(board)