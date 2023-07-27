import random
import time

grids = [['', '', ''], ['', '', ''], ['', '', '']]
formatGrids = ("  1  2  3",
               "A ", grids[0][0], "  ", grids[0][1], "  ", grids[0][2], "\n",
               "B ", grids[1][0], "  ", grids[2][1], "  ", grids[2][2], "\n",
               "C ", grids[2][0], "  ", grids[1][1], "  ", grids[2][2], "\n")


#   1  2  3
# A X  X  X
# B X  X  X
# C X  X  X


def player_turn():
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
            if grids[gi[0]][gi[1]] == '':
                grids[gi[0]][gi[1]] = 'X'
                # print(grids[gi[0]][gi[1]])
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
        # print grid here
    # else:
    #     system_turn()


if __name__ == "__main__":
    tictactoe_prompt()
