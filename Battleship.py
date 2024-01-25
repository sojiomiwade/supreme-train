import random

class Ship:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.coordinates = []

    def place_ship(self, coordinates):
        self.coordinates = coordinates


class Board:
    def __init__(self, size):
        self.size = size
        self.grid = [['O' for _ in range(size)] for _ in range(size)]

    def display(self):
        for row in self.grid:
            print(' '.join(row))

    def place_ship(self, ship):
        for coord in ship.coordinates:
            x, y = coord
            self.grid[x][y] = 'S'

    def is_valid_move(self, x, y):
        return 0 <= x < self.size and 0 <= y < self.size and self.grid[x][y] == 'O'


class Player:
    def __init__(self, name):
        self.name = name
        self.board = Board(10)
        self.ships = []

    def place_ship(self, ship, coordinates):
        ship.place_ship(coordinates)
        self.ships.append(ship)
        self.board.place_ship(ship)

    def make_move(self, x, y, opponent_board):
        if opponent_board.is_valid_move(x, y):
            return True
        else:
            print("Invalid move. Try again.")
            return False


class BattleshipGame:
    def __init__(self, player1_name, player2_name):
        self.player1 = Player(player1_name)
        self.player2 = Player(player2_name)

    def randomly_place_ships(self, player, ship):
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        orientation = random.choice(['horizontal', 'vertical'])

        ship_coordinates = []

        for _ in range(ship.size):
            ship_coordinates.append((x, y))
            if orientation == 'horizontal':
                y += 1
            else:
                x += 1

        player.place_ship(ship, ship_coordinates)

    def play(self):
        print("Battleship Game Started!")
        self.randomly_place_ships(self.player1, Ship("Carrier", 5))
        self.randomly_place_ships(self.player1, Ship("Battleship", 4))
        self.randomly_place_ships(self.player2, Ship("Submarine", 3))
        self.randomly_place_ships(self.player2, Ship("Destroyer", 3))

        while True:
            self.player1.board.display()
            print("\n" + "-" * 20 + "\n")
            self.player2.board.display()

            x1, y1 = map(int, input(f"{self.player1.name}, enter your move (row column): ").split())
            while not self.player1.make_move(x1, y1, self.player2.board):
                x1, y1 = map(int, input(f"{self.player1.name}, enter your move (row column): ").split())

            if self.check_winner(self.player2):
                print(f"Congratulations! {self.player1.name} wins!")
                break

            x2, y2 = map(int, input(f"{self.player2.name}, enter your move (row column): ").split())
            while not self.player2.make_move(x2, y2, self.player1.board):
                x2, y2 = map(int, input(f"{self.player2.name}, enter your move (row column): ").split())

            if self.check_winner(self.player1):
                print(f"Congratulations! {self.player2.name} wins!")
                break

    def check_winner(self, opponent):
        for ship in opponent.ships:
            for coord in ship.coordinates:
                x, y = coord
                if opponent.board.grid[x][y] != 'X':
                    return False
        return True


if __name__ == "__main__":
    game = BattleshipGame("Player1", "Player2")
    game.play()
