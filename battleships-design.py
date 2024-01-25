import random

def print_board(board):
    for row in board:
        print(" ".join(row))

def generate_ship(board):
    ship_row = random.randint(0, len(board) - 1)
    ship_col = random.randint(0, len(board[0]) - 1)
    return ship_row, ship_col

def play_battleship():
    board_size = 5
    num_ships = 1

    # Initialize the board
    board = [["O" for _ in range(board_size)] for _ in range(board_size)]

    # Place the ships on the board
    ships = []
    for _ in range(num_ships):
        ship = generate_ship(board)
        while ship in ships:
            ship = generate_ship(board)
        ships.append(ship)

    attempts = 0

    print("Let's play Battleship!")
    print_board(board)

    while True:
        # Get user input for a guess
        guess_row = int(input("Guess Row: "))
        guess_col = int(input("Guess Col: "))
        
        if guess_row < 0 or guess_row >= board_size or guess_col < 0 or guess_col >= board_size:
            print("Oops, that's not even in the ocean. Try again.")
            continue

        attempts += 1

        # Check if the guess is a hit or miss
        if (guess_row, guess_col) in ships:
            print("Congratulations! You sank my battleship!")
            break
        else:
            if board[guess_row][guess_col] == "X":
                print("You guessed that one already.")
            else:
                print("You missed my battleship!")
                board[guess_row][guess_col] = "X"
            
            print_board(board)

    print(f"You made {attempts} attempts.")

if __name__ == "__main__":
    play_battleship()
