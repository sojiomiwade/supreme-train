import random
from typing import List, Set, Tuple

def get_one_guess():
    # Get user input for a guess
    guess=input('guess row and col: ').split()
    return int(guess[0]),int(guess[1])

def print_board(board: List[List[str]]) -> None:
    for row in board:
        print(" ".join(row))

def generate_one_ship_loc(board) -> Tuple[int, int]:
    ship_row = random.randrange(len(board))
    ship_col = random.randrange(len(board[0]))
    return ship_row, ship_col

def place_ships(board, num_ships) -> Set[Tuple[int, int]]:
    # Place the ships on the board
    ships = set()
    for _ in range(num_ships):
        ship = generate_one_ship_loc(board)
        while ship in ships:
            ship = generate_one_ship_loc(board)
        ships.add(ship)
    return ships

def process_guess(board,guess_row,guess_col,ships) -> None:
    # Check if the guess is a hit or miss
    if (guess_row, guess_col) in ships:
        board[guess_row][guess_col]='B'
        print("Congratulations! You sank a battleship!")
        ships.remove((guess_row,guess_col))
    else:
        if board[guess_row][guess_col] != "O":
            print("You guessed that one already.")
        else:
            print("You missed my battleship!")
            board[guess_row][guess_col] = "X"

def play_battleship(board_size,num_ships):    

    # Initialize the board
    board = [["O" for _ in range(board_size)] for _ in range(board_size)]
    attempts = 0

    print("Let's play Battleship!")
    print_board(board)
    ships=place_ships(board,num_ships)
    while ships:
        guess_row,guess_col=get_one_guess()
        if guess_row < 0 or guess_row >= board_size or guess_col < 0 or guess_col >= board_size:
            print("Oops, that's not even in the ocean. Try again.")
            continue

        attempts += 1
        process_guess(board,guess_row,guess_col,ships)            
        print_board(board)

    print(f"You made {attempts} attempts.")

if __name__ == "__main__":
    board_size = 2
    num_ships = 2
    play_battleship(board_size,num_ships)
