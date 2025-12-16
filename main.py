import random
game = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]

def game_board() -> None:
    """
    Display the current game board with column indices.

    Prints a 3x3 grid representing the current state of the game,
    including column headers for reference.

    Returns:
        None
    """
    print("    0    1    2")
    for column, row in enumerate(game):
        print(column, row)

def moves(col: int, row: int, player: str) -> bool:
    """
    Attempt to place a player's mark on the game board.

    Places the player's symbol at the specified row and column
    if the cell is empty.

    Args:
        col (int): Column index (0-2).
        row (int): Row index (0-2).
        player (str): Player symbol (e.g., 'X' or 'O').

    Returns:
        bool: True if the move was successful, False if the cell was already used.
    """
    if game[row][col] == "_":
        game[row][col] = player
        return True
    else:
        print("The block have already being used.")
        return False

def results(player: str) -> bool:
    """
    Check whether the given player has won the game.

    Evaluates all rows, columns, and diagonals to determine
    if the player has three matching symbols in a line.

    Args:
        player (str): Player symbol to check.

    Returns:
        bool: True if the player has won, False otherwise.
    """
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

def draw() -> bool:
    """
    Determine whether the game has ended in a draw.

    A draw occurs when all cells are filled and no player
    has won the game.

    Returns:
        bool: True if the game is a draw, False otherwise.
    """
    for row in game:
        if "_" in row:
            return False
    return True


# Main code:
def main():
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

if __name__ == "__main__":
    main()