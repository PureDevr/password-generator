import random
import time

GRID = [['', '', 'X'], ['', '', ''], ['', '', '']]


def format_grid(gi0, gi1, side):
    GRID[gi0][gi1] = side
    formatGrid = ("  1  2  3\n",
                  "A ", GRID[0][0], "   ", GRID[0][1], "   ", GRID[0][2], "\n",
                  "B ", GRID[1][0], "   ", GRID[2][1], "   ", GRID[2][2], "\n",
                  "C ", GRID[2][0], "   ", GRID[1][1], "   ", GRID[2][2], "\n")

    # print(GRIDS)
    # print(formatGrids)
    printGrid = ''.join(e for e in formatGrid)
    print(printGrid)


#   1  2  3
# A X  X  X
# B X  X  X
# C X  X  X


def player_turn():
    printedGrid = ''
    while True:
        print("Input your choice:")
        user_input = input("> ")
        gi = [None, None]  # "gi" stands for grid index
        if (user_input[0] in ['A', 'B', 'C']) and (user_input[1] in ['1', '2', '3']):
            match user_input[0]:
                case 'A':
                    gi[0] = 0
                case 'B':
                    gi[0] = 1
                case 'C':
                    gi[0] = 2
            match user_input[1]:
                case '1':
                    gi[1] = 0
                case '2':
                    gi[1] = 1
                case '3':
                    gi[1] = 2
            if GRID[gi[0]][gi[1]] == '':
                format_grid(gi[0], gi[1], 'X')
                print("test")
                break
        print("ERROR: Please enter an empty grid in the format of: A1.")


# def system_turn():


def tictactoe_prompt():
    print("Tic Tac Toe: First to form a line wins.\nYOU: X\tSYSTEM: O\n\nDeciding which side goes first", end='')
    for _ in range(3):
        time.sleep(1)
        print('.', end='', flush=True)
    time.sleep(3)
    xo = ['X', 'O']
    first = random.choice(xo)
    print(first)  # computer decide and print which side goes first
    if first == 'X':
        player_turn()

    # else:
    #     system_turn()


if __name__ == "__main__":
    player_turn()
