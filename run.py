# Key for map

# X = position and hit
# ' ' = free space
# '-' = missed shot

from random import randint

#Boards
SECRET_BOARD = [[''] * 8 for x in range(8)]
PLAYER_BOARD = [[''] * 8 for x in range(8)]

letters_to_numbers = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7,}

def create_board(board):
    print('  A B C D E F G H')
    print('  ---------------')
    
    row_number = 1
    for row in board:

       print("%d¦%s¦" % (row_number, "¦" .join(row)))
       row_number += 1

def random_ship_location(board):
    for ship in range (5):
        ship_row, ship_column = randint(0, 7), randint(0, 7)
        while [ship_row] [ship_column] == 'X':
            ship_row, ship_column = randint(0, 7), randint(0, 7)
        board[ship_row][ship_column] = 'X'


def guess_ship_location():
    row = input('Where will you fire your cannons?!? 1 - 8')
    while row not in '12345678': 
        print("Your shots must fired on the map, between 1 - 8")
        row = input('Where will you fire your cannons?!? 1 - 8')

    column = input('Where will you fire your cannons?!? A - H').upper()
    while column not in 'ABCDEFGH':
        print("Your shots must fired on the map, between A - H")
        column = input('Where will you fire your cannons?!? A - H').upper()

    return int(row) - 1, letters_to_numbers[column]

# Need a way to stop User from not inputting anything




def ship_hits(board):
    count = 0
    for rows in board:
        for column in row:
            if column == 'X':
                count +=1
    return count







random_ship_location(SECRET_BOARD)

turns = 10
# while turns > 0 

create_board(SECRET_BOARD)
create_board(PLAYER_BOARD)
