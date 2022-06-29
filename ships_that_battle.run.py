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


username = input("Captain, what's your name? ")
print_message(username)


message = "Enter your coordinates on the map \
to sink the enemy's fleet.\
 First, choose a row between 1 - 8, then a column between A - H. \
 GOOD LUCK!"

print(message)

# Boards
secret_board = [[' '] * 8 for x in range(8)]
player_board = [[' '] * 8 for x in range(8)]

letters_to_numbers = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4,
                      'F': 5, 'G': 6, 'H': 7}


def create_board(board):
    '''
    This function creates the layout of the board
    '''
    
    print('    A   B   C   D   E   F   G   H')
    print('  +-------------------------------+')
    row_number = 1
    for row in board:
        print("%d | %s | " % (row_number, " | ".join(row)))
        row_number += 1
    print('  +-------------------------------+')



def random_ship_location(board):
    '''
    This function places 5 ships at random on secret_board
    '''
    for ship in range(5):
        ship_row, ship_column = randint(0, 7), randint(0, 7)
        while board[ship_row][ship_column] == 'X':
            ship_row, ship_column = randint(0, 7), randint(0, 7)
    board[ship_row][ship_column] = 'X'



def guess_ship_location():
    '''
    This function checks that input is valid and returns coordinates
    '''
    row = input('Captain, where will you fire your cannons?!? 1 - 8: ')
    while row not in '12345678':
        print("Your shots must be fired on the map, between rows 1 - 8")
        row = input('Where will you fire your cannons?!? row 1 - 8: ')
    column = input('Where will you fire your cannons?!? A - H: ').upper()
    while column not in 'ABCDEFGH':
        print("Your shots must fired on the map, between A - H")
        column = input('Where will you fire your cannons?!? A - H: ').upper()
    return int(row) - 1, letters_to_numbers[column]


def all_ships_hit(board):
    '''
    This function tracks and adds up hits
    '''
    count = 0
    for row in board:
        for column in row:
            if column == 'X':
                count += 1
    return count


# Tracks hits, misses and repeated coordinates
random_ship_location(secret_board)
turns = 3
create_board(secret_board)
while turns > 0:
    print("Fire at the Enemy to sink their ships")
    create_board(player_board)
    row, column = guess_ship_location()
    if player_board[row][column] == '-':
        print("Deja Vu, try a different location on the map")
    elif secret_board[row][column] == 'X':
        print("Huzzah, a hit!")
        player_board[row][column] = 'X'
        turns -= 1
    else:
        print("A miss, and a splash. Better luck next turn!")
        player_board[row][column] = "-"
        turns -= 1
    if all_ships_hit == 5:
        print("Congratulations Captain, you rule the waves!")
        break
    print("Captain, you have " + str(turns) + " cannon balls left")
    if turns == 0:
        print("Captain, it's too late, you ran out of cannonballs.\
        GAME OVER!")


def new_game():
    create_board(secret_board)
    create_board(player_board)


new_game()
