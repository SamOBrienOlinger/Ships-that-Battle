"""
Key for map

X = hit
' ' = free space
'-' = missed shot

Messages for Player

"Deja Vu, try a different location on the map" = \
    enter a row number and column letter not previously used
"Congratulations Captain, you rule the waves!" = \
    Player wins
"Captain, it's too late, you ran out of cannonballs" = \
    Player loses

"""
from random import randint


def print_message(name):
    print(f"Welcome Captain {name}")

username = input("What's your name? ")
print_message(username)


message = "Enter your coordinates on the map \
to sink the enemy's fleet.\
 First, choose a row between 1 - 8, then a column between A - H. \
 GOOD LUCK!"

print(message)

# Boards
SECRET_BOARD = [[''] * 8 for x in range(8)]
PLAYER_BOARD = [[''] * 8 for x in range(8)]

letters_to_numbers = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4,
                      'F': 5, 'G': 6, 'H': 7}

# board = SECRET_BOARD, PLAYER_BOARD


def create_board(board):
    print('    A  B  C  D  E  F  G  H')
    print('   +-----------------------+')
    row_number = 1
    for row in board:
        print("%d  | %s |" % (row_number, " | ".join(row)))
        row_number += 1
    print('   +-----------------------+')


# Place 5 random ships on SECRET_BOARD
def random_ship_location(board):
    for x in range(5):
        ship_row, ship_column = randint(0, 7), randint(0, 7)
        while board[ship_row][ship_column] == 'X':
            ship_row, ship_column = guess_ship_location()
    board[ship_row][ship_column] = 'X'


# Checks that input is valid and returns input
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

# Tracks and adds up hits

def all_ships_hit(board):
    count = 0
    for row in board:
        for column in row:
            if column == 'X':
                count += 1
    return count


# Tracks hits, misses and repeated coordinates
random_ship_location(SECRET_BOARD)
create_board(SECRET_BOARD)
turns = 3
while turns > 0:
    print("Fire at the Enemy to sink their ships")
    create_board(PLAYER_BOARD)
    row, column = guess_ship_location()
    if PLAYER_BOARD[row][column] == '-':
        print("Deja Vu, try a different location on the map")
    elif SECRET_BOARD[row][column] == 'X':
        print("Huzzah, a hit!")
        PLAYER_BOARD[row][column] = 'X'
        turns -= 1
    else:
        print("A miss, and a splash. Better luck next turn!")
        PLAYER_BOARD[row][column] = "-"
        turns -= 1
    if all_ships_hit == 5:
        print("Congratulations Captain, you rule the waves!")
        break
    print("Captain, you have " + str(turns) + " cannon balls left")
    if turns == 0:
        print("Captain, it's too late, you ran out of cannonballs.\
        GAME OVER!")

# hits_and_misses(board)


def new_game():
    create_board(SECRET_BOARD)

new_game()


# all_ships_hit(board=)

# print(hits_and_misses(PLAYER_BOARD))
# hits_and_misses(board=PLAYER_BOARD)

# create_board(PLAYER_BOARD)
