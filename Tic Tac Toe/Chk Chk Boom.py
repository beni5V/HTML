board = ['1', '2', '3',
         '4', '5', '6',
         '7', '8', '9']


def display_board():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()


def check_winner(player):
    win_positions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], 
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  
        [0, 4, 8], [2, 4, 6]              
    ]

    for position in win_positions:
        if (board[position[0]] == board[position[1]] ==
                board[position[2]] == player):
            return True
    return False


def is_draw():
    for cell in board:
        if cell not in ['X', 'O']:
            return False
    return True


player = 'X'

while True:
    display_board()

    choice = int(input(f"Player {player}, enter a position (1-9): "))

    if choice < 1 or choice > 9:
        print("Invalid position! Try again.")
        continue

    if board[choice - 1] == 'X' or board[choice - 1] == 'O':
        print("Position already taken! Try again.")
        continue

    board[choice - 1] = player

    if check_winner(player):
        display_board()
        print(f"🎉 Player {player} wins!")
        break

    if is_draw():
        display_board()
        print("🤝 It's a draw!")
        break

    if player == 'X':
        player = 'O'
    else:
        player = 'X'