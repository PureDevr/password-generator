import random
import time

GRID = [[' ', ' ', ' '], ['X', ' ', ' '], ['X', ' ', ' ']]  # 3x3 grid left to right, up to down


def line_check():  # check for connected lines = one side win
    if any(GRID[n1][0] == GRID[n1][1] == GRID[n1][2] for n1 in range(3)) or \
       any(GRID[0][n2] == GRID[1][n2] == GRID[2][n2] for n2 in range(3)) or \
       (GRID[0][0] == GRID[1][1] == GRID[2][2]) or \
       (GRID[0][2] == GRID[1][1] == GRID[2][0]):  # check for horizontal, vertical, both slant lines
        return 1  # return 1 back to whoever turn function that called this, notifying that the side won.
    return


def print_grid(gi0, gi1, side):  # the to-be-changed grid's 2D index and side (X or O)
    GRID[gi0][gi1] = side
    formatGrid = ("   1  2  3\n",
                  "A  ", GRID[0][0], "  ", GRID[0][1], "  ", GRID[0][2], "\n",
                  "B  ", GRID[1][0], "  ", GRID[2][1], "  ", GRID[2][2], "\n",
                  "C  ", GRID[2][0], "  ", GRID[1][1], "  ", GRID[2][2], "\n")
    # This is what the printed grid looks like:
    #    1  2  3
    # A  X  X  X
    # B  X  X  X
    # C  X  X  X
    printGrid = ''.join(e for e in formatGrid)  # put everything into 1 string
    print(printGrid)  # output the updated grid


def player_turn():
    printedGrid = ''
    while True:  # infinite loop in the case of dummy-input
        print("Input your choice:")
        user_input = input("> ")
        gi = [None, None]  # "gi" stands for grid index, to be sent to print_grid to notify grid update
        if (user_input[0] in ['A', 'B', 'C']) and (user_input[1] in ['1', '2', '3']):  # input dummy-proof
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
            if GRID[gi[0]][gi[1]] == '':  # if the user selected grid is empty
                print_grid(gi[0], gi[1], 'X')  # finally call to update and print new grid
                if line_check() == 1:  # call line check see if there is a line connected
                    print("You won!")
                    return  # return to tictactoe_prompt (which will redirect back to main.py)
                break  # if no line, break out of this while loop and call system_turn() to switch side
        print("ERROR: Please enter an empty grid in the format of: A1.")  # if dummy input, error and restart while tru
    system_turn()


def system_turn():
    return


def tictactoe_prompt():
    print("Tic Tac Toe: First to form a line wins.\nYOU: X\tSYSTEM: O\n\nDeciding which side goes first", end = '')
    for _ in range(3):
        time.sleep(1)
        print('.', end='', flush=True)
    time.sleep(3)
    xo = ['X', 'O']
    first = random.choice(xo)
    print(first)  # computer decide and print which side goes first
    if first == 'X':  # this is where it starts. flow won't come back to this function until the end.
        player_turn()
    else:
        system_turn()
    return


if __name__ == "__main__":
    print_grid(0, 0, 'X')
