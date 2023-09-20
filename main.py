## This is a Tabnine-generated program to play tic-tac-toe. It is a placeholder for the structure of a turn-based Pykémon battle.

if "__name__" == "__main__":
    while(victory := False):
        board = Board()
        player = Player(board)
        computer = Computer(board)

        while not victory:
            print(board)
            player_move = player.get_move()
            computer_move = computer.get_move()

            if player_move == computer_move:
                print("Tie!")
            elif player_move == "X":
                board.mark_board(player_move)
            elif player_move == "O":
                board.mark_board(computer_move)
            else:
                print("Invalid move!")

            if board.is_board_full():
                victory = True

        print(board)
        print(f"Winner: {board.get_winner()}")