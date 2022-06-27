"""
Key for map

X = hit
' ' = free space
'-' = missed shot

Messages for Player

"Deja Vu, try a different location on the map" = enter a row number and column letter not previously used
"Congratulations Captain, you rule the waves!" = Player wins
"Captain, it's too late, you ran out of cannonballs" = Player loses

"""
from random import randint

message = ["Welcome, Captain. Enter your coordinates on the map to sink the enemy's fleet"]
print(message)

# Boards
SECRET_BOARD = [[''] * 8 for x in range(8)]
PLAYER_BOARD = [[''] * 8 for x in range(8)]

letters_to_numbers = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4,
                      'F': 5, 'G': 6, 'H': 7}


def create_board(board):
    print('  A B C D E F G H')
    print('  ---------------')
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1


# Place 5 random ships on SECRET_BOARD
def random_ship_location(board):
    for ship in range(5):
        ship_row, ship_column = randint(0, 7), randint(0, 7)
        while board[ship_row][ship_column] == 'X':
            ship_row, ship_column = guess_ship_location()
    board[ship_row][ship_column] = 'X'


def guess_ship_location():
    row = input('Where will you fire your cannons?!? 1 - 8: ')
    while row not in '12345678':
        print("Your shots must be fired on the map, between rows 1 - 8")
        row = input('Where will you fire your cannons?!? row 1 - 8: ')
    column = input('Where will you fire your cannons?!? A - H: ').upper()
    while column not in 'ABCDEFGH':
        print("Your shots must fired on the map, between A - H")
        column = input('Where will you fire your cannons?!? A - H: ').upper()
    return int(row) - 1, letters_to_numbers[column]

# Need code that handles empty or invalid input data.


def all_ships_hit(board):
    count = 0
    for row in board:
        for column in row:
            if column == 'X':
                count += 1
    return count

# Tracks hits, misses and repeated coordinates 
if __name__ == "__main__":
    random_ship_location(SECRET_BOARD)
    turns = 10
    while turns > 0:
        print("Fire at the Enemy to Battle their Ships")
        print(PLAYER_BOARD)
        row, column = guess_ship_location()
        if SECRET_BOARD[row][column] == '-':
            print("Deja Vu, try a different location on the map")
        elif SECRET_BOARD[row][column] == "X":
            print("Huzzah, a hit!")
            PLAYER_BOARD[row][column] = "X"
            turns -= 1
        else:
            print("A miss, and a splash. Better luck next turn!")
            SECRET_BOARD[row][column] = "-"
            turns -= 1
        if all_ships_hit == 5:
            print("Congratulations Captain, you rule the waves!")
            break
        print("Captain, you have " + str(turns) + " cannon balls left")
        if turns == 0:
            print("Captain, it's too late, you ran out of cannonballs")



def new_game():
        print(
        "Welcome, Captain. Enter your coordinates on the map to sink the enemy's fleet"
        )
    create_board(SECRET_BOARD)
    create_board(PLAYER_BOARD)

new_game()