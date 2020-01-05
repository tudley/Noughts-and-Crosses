def check_for_win(board, x, o):
    winning_board = [(board[0], board[1], board[2]),
                     (board[3], board[4], board[5]),
                     (board[6], board[7], board[8]),
                     (board[0], board[3], board[6]),
                     (board[1], board[4], board[7]),
                     (board[2], board[5], board[8]),
                     (board[0], board[4], board[8]),
                     (board[2], board[4], board[6])]
    if (x, x, x) in winning_board:
        print('x win')
        return True
    elif (o, o, o) in winning_board:
        print(' o win')
        return True
    else:
        return False


def pick_position(board, player, symbol):
    while True:
        player_row = int(input(player + ' pick your row'))
        while player_row not in (1, 2, 3):
            player_row = int(input('row not recognised, input again: '))
        player_column = int(input(player + ' pick your column'))
        while player_column not in (1, 2, 3):
            player_column = int(input('column not recognised, input again: '))

        choice = ''

        if player_row == 1:
            choice = 0
        elif player_row == 2:
            choice = 3
        elif player_row == 3:
            choice = 6

        if player_column == 1:
            choice += 0
        elif player_column == 2:
            choice += 1
        elif player_column == 3:
            choice += 2

        if board[choice] == ' ':
            board[choice] = symbol
            break
        else:
            print('position already taken, try again.')


grid = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
print(str(grid[:3]) + '\n' + str(grid[3:6]) + '\n' + str(grid[6:]))
print('the board is set up so row 1, column 1 is the top left square, and row 3 column 3 is the bottom right square')

while True:
    pick_position(grid, 'player 1', 'X')
    print(str(grid[:3]) + '\n' + str(grid[3:6]) + '\n' + str(grid[6:]))
    x_win = check_for_win(grid, 'X', 'O')
    if x_win:
        break

    pick_position(grid, 'player 2', 'O')
    print(str(grid[:3]) + '\n' + str(grid[3:6]) + '\n' + str(grid[6:]))
    o_win = check_for_win(grid, 'X', 'O')
    if o_win:
        break
