import random
game = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]

def game_board():
    print("    0    1    2")
    for column, row in enumerate(game):
        print(column, row)

def moves(col, row, player):
    if game[row][col] == "_":
        game[row][col] = player
        return True
    else:
        print("The block have already being used.")
        return False

def results(player):
    # row
    for row in game:
        if row == [player, player, player]:
            return True

    # column
    for col in range(3):
        if game[0][col] == game[1][col] == game[2][col] == player:
            return True

    # diagonal
    if game[0][0] == game[1][1] == game[2][2] == player:
        return True
    elif game[0][2] == game[1][1] == game[2][0] == player:
        return True
    else:
        return False

def draw():
    for row in game:
        if "_" in row:
            return False
    return True


# Main code:
game_board()
game_on = True

playerX = "X"
playerO = "O"
current_player = random.choice([playerX, playerO])

while game_on:
    print(f"{current_player}'s turn: ")
    col_move = int(input("Enter the column: "))
    row_move = int(input("Enter the row: "))
    if not moves(col_move, row_move, current_player):
        continue
    game_board()
    #  Check results
    if results(current_player):
        print(f"{current_player} won the game!")
        game_on = False
        break

    if draw():
        print(f"Both players 'X' and 'O' did well, but its a draw!")
        break

    # Switching player:
    if current_player == playerX:
        current_player = playerO
    else:
        current_player = playerX