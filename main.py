from Minesweeper import Minesweeper


class main():
    board = Minesweeper(4, 4, 3)
    print(board)

    board.placeBomb()
    board.placeNumbers()
    print(board.board)
    print(board.playerBoard)
    while True:
        x = int(input("Enter y: "))
        y = int(input("Enter x: "))
        action = int(input("Enter 1 to reveal, 2 to flag: "))
        if action == 1:
            if board.reveal(x, y):
                print("You lost!")
                break
        elif action == 2:
            board.flag(x, y)
        print(board.playerBoard)

        if board.checkWin():
            print("You won!")
            break