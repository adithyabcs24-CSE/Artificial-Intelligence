# Tic Tac Toe - Human (X) vs Computer (O)
# Computer uses Minimax algorithm

# Create empty 3x3 board
board = [" " for _ in range(9)]


# Display the current board
def display_board():
    print()
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("---+---+---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("---+---+---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])
    print()


# Check whether a player has won
def check_winner(player):
    winning_combinations = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in winning_combinations:
        if board[a] == player and board[b] == player and board[c] == player:
            return True

    return False


# Check whether the board is full
def is_board_full():
    return " " not in board


# Minimax algorithm
def minimax(is_maximizing):
    
    # Computer wins
    if check_winner("O"):
        return 1

    # Human wins
    if check_winner("X"):
        return -1

    # Draw
    if is_board_full():
        return 0

    if is_maximizing:
        best_score = -float("inf")

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"

                score = minimax(False)

                board[i] = " "

                best_score = max(best_score, score)

        return best_score

    else:
        best_score = float("inf")

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"

                score = minimax(True)

                board[i] = " "

                best_score = min(best_score, score)

        return best_score


# Find the best move for computer
def find_best_move():
    best_score = -float("inf")
    best_move = None

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"

            score = minimax(False)

            board[i] = " "

            if score > best_score:
                best_score = score
                best_move = i

    return best_move


# Human plays as X
def human_move():
    while True:
        try:
            position = int(input("Enter your position (1-9): "))

            # Check valid position
            if position < 1 or position > 9:
                print("Invalid position! Enter a number from 1 to 9.")
                continue

            index = position - 1

            # Check whether position is empty
            if board[index] != " ":
                print("Position already occupied! Try again.")
                continue

            # Put X on board
            board[index] = "X"
            break

        except ValueError:
            print("Please enter a valid number.")


# Main game
def play_game():

    print("===== TIC TAC TOE =====")
    print("You are X")
    print("Computer is O")

    while True:

        # Display current board
        display_board()

        # Human plays X
        human_move()

        # Did X win?
        if check_winner("X"):
            display_board()
            print("Congratulations! You win!")
            print("GAME OVER")
            break

        # Is board full?
        if is_board_full():
            display_board()
            print("DRAW!")
            break

        # Computer plays O
        print("Computer is thinking...")

        # Minimax finds best move
        computer_move = find_best_move()

        # Put O on board
        board[computer_move] = "O"

        # Display board after computer move
        display_board()

        # Did O win?
        if check_winner("O"):
            print("Computer wins!")
            print("GAME OVER")
            break

        # Is board full?
        if is_board_full():
            print("DRAW!")
            break

        # Repeat
        print("Your turn!")


# Start the game
play_game()