import random 
import enum 


# Defining an enum for player/ computer sympols 
class Symbols(enum.Enum):
     Player = "P"
     Computer = "C"

# Game symbols 
SYMBOL_PLAYER = "P"
SYMBOL_COMPUTER = "C"
SYMBOL_EMPTY = "."
SYMBOL_HIT = "X"
SYMBOL_MISS = "O"

# Initialize player and computer stats 
player_counter = 0
computer_counter = 0
player_no_of_hits = 0
computer_no_of_hits = 0

# Function to print the grid 
def print_grid(grid, symbols_to_hide=["B"]):
        print("   A B C D E F ")
        print("  |_|_|_|_|_|_| ") 
        row_number = 1
        for row in grid:
            print_row = []
            for char in row:
                 if char in symbols_to_hide:
                      char = SYMBOL_COMPUTER
                 print_row.append(char)
            print(f"{row_number} |" + "|".join(print_row) + "|")
            row_number += 1


# Function to randomly place ships on the grid
def place_ships(grid, no_of_ships, ship_symbol):
    ships_placed = 0
    grid_size = len(grid[1]) * len(grid)
    while ships_placed < no_of_ships:
        loc = random.randint(0, grid_size - 1) 
        row = loc // len(grid[1]) 
        col = loc % len(grid[1]) 
        if grid[row][col] == SYMBOL_EMPTY: 
           grid[row][col] = ship_symbol 
           ships_placed += 1 
     
# Allowing the player to attack
def player_attack(computer_grid):
     while True:
          try:
               move = input("Enter your attack (e.g., A5): \n").upper()
               col = ord(move[0]) - 65 
               row = int(move[1:]) - 1 
               if computer_grid[row][col] == SYMBOL_COMPUTER:
                    print("You hit a ship!")
                    computer_grid[row][col] = SYMBOL_HIT
                    return True 
               elif computer_grid[row][col] == SYMBOL_EMPTY:
                    print("You Missed!")
                    computer_grid[row][col] = SYMBOL_MISS
                    return False 
               else:
                    print("You've already attacked this area! Try again.")
          except (IndexError, ValueError): 
               print("Invalid Input. Please enter a valid attack strategy. Your input must include a letter, followed by a number (e.g., A5).")


# Allowing the computer to attack 
def computer_attack(player_grid):
     while True:
          row = random.randint(0, len(player_grid) - 1)
          col = random.randint(0, len(player_grid[0]) - 1)
          if player_grid[row][col] == SYMBOL_PLAYER: 
               print(f"Computer hits at {chr(col + 65)}{row + 1}!")
               player_grid[row][col] = SYMBOL_HIT
               return True 
          elif player_grid[row][col] == SYMBOL_EMPTY:
               print(f"Computer hits at {chr(col + 65)}{row + 1}.")
               player_grid[row][col] = SYMBOL_MISS
               return False

# Starting the game
def start_game():
     global player_no_of_hits, computer_no_of_hits

     print("Preparing For Battle!")

     # Creating a 10x10 grid for player and computer
     grid_size = 6
     player_grid = [[SYMBOL_EMPTY for _ in range(grid_size)] for _ in range(grid_size)]
     computer_grid = [[SYMBOL_EMPTY for _ in range(grid_size)] for _ in range(grid_size)]
     
     # Place 5 ships on each board 
     print('\nPreparing Your Battleships...')
     place_ships(player_grid, 4, SYMBOL_PLAYER)
     print("Preparing Your Opponent's Battleships...")
     place_ships(computer_grid, 4, SYMBOL_COMPUTER)

     # Game Loop
     while player_no_of_hits < 5 and computer_no_of_hits < 5:
          print("\nYour Battlefield:")
          print_grid(player_grid)
          print("\nOpponent's battlefield is hidden:")
          print_grid([[SYMBOL_EMPTY if cell == SYMBOL_COMPUTER else cell for cell in row] for row in computer_grid])

          print("\nThe Battle has begun. Make your move!")

          # Player's turn 
          print("\nYour turn!")
          if player_attack(computer_grid):
               player_no_of_hits += 1
          print(f"Your hits: {player_no_of_hits}")

          # Check if the player won 
          if player_no_of_hits == 4:
               print("Well Done! You've sunk your opponent's battleships. You Win!")
               break

          # Computer's turn 
          print("\nComputer's turn!")
          if computer_attack(player_grid):
               computer_no_of_hits +=1
          print(f"Computer's hits: {computer_no_of_hits}")

          # Check if the computer has won 
          if computer_no_of_hits == 4:
               print("Your ships have been destroyed. You Lost!")
               break 


if __name__ == "__main__":
               start_game()       