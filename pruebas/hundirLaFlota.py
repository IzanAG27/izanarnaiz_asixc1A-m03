import numpy as np

def create_board(rows, cols):
    return np.full((rows, cols), '🌊')

def print_board(board):
    for row in board:
        print(' '.join(row))

def place_ships(board, ships):
    for _ in range(ships):
        while True:
            print_board(board)
            print("Enter the coordinates to place your ship (format: row col) or type '\\q' to finish: ")
            user_input = input()
            if user_input == '\\q':
                return
            row, col = map(int, user_input.split())
            if board[row][col] == '🌊':
                board[row][col] = '🚢'
                break
            else:
                print("Invalid position. Try again.")

def attack(board, row, col):
    if board[row][col] == '🚢':
        board[row][col] = '💥'
        print("Hit!")
        return True
    else:
        board[row][col] = '❌'
        print("Miss!")
        return False

def play_game(rows=10, cols=10, ships=5):
    board = create_board(rows, cols)
    place_ships(board, ships)
    print("Press enter to start attacking.")
    input()
    while True:
        print_board(board)
        row, col = map(int, input("Enter row and col to attack: ").split())
        if not attack(board, row, col):
            if '🚢' not in board:
                print("Congratulations, you won! 🎉")
                break

play_game()