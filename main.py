from modules.app1_password_gen import password_gen_prompt
from modules.app2_character_sorter import char_sorter_prompt
from modules.app3_num_guesser import num_guesser_prompt
from modules.app4_tictactoe import tictactoe_prompt

if __name__ == '__main__':
    while True:
        while True:  # infinite loop until the break
            # asks user the length of the password
            listOfApps: list[str] = ["Password Generator-------1", "Object Sorter------------2",
                                     "Number Guesser-----------3", "Tic Tac Toe--------------4",
                                     "Exit App-----------------0"]
            print("Select the application:")
            for app in listOfApps:
                print(app)
            user_input = input("> ")
            user_choice = ''.join(c for c in user_input if c.isnumeric())
            if len(user_choice) > 0:
                if 0 <= int(user_choice) <= len(listOfApps):
                    break  # break after there's a numeric & legit length

        user_choice = int(user_choice)
        match int(user_choice):
            case 0:
                break
            case 1:
                password_gen_prompt()
            case 2:
                char_sorter_prompt()
            case 3:
                num_guesser_prompt()
            case 4:
                tictactoe_prompt()
