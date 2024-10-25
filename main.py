def printboard(board):
    print(board)

def tic_tac_toe():
    print("Hello, Tic Tac Toe!")
    # Step 1: Print any introductory message

    # Step 2: Create a list to represent the board
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

    board_string = """
    {0} | {1} | {2}
    ---------
    {3} | {4} | {5}
    ---------
    {6} | {7} | {8}
    """

    # Step 3: Create a loop to alternate between players
    player1_turn = True
    gameover = False
    while not gameover:
        # Step 4: Get the player's input 
        try: 
            userinput = int(input())
        except ValueError:
            print("Please pick a number between 1 and 9")
            continue

        # Step 5: Check if the player's input is valid
        if userinput >= 10 or userinput <= 0:
            print("Please pick a number between 1 and 9") 
            continue

        # Step 6: Check if the player has won

        # Step 7: Check if the board is full
    
        # Step 8: Print the board
        print(board_string.format(*board))

    # Step 9: Print the result of the game

def main():
    tic_tac_toe()

if __name__ == "__main__":
    main()
