from typing import List

from modules.app1_password_gen import password_gen_prompt
from modules.app2_character_sorter import char_sorter_prompt
from modules.app3_num_guesser import num_guesser_prompt

if __name__ == '__main__':

    while True:  # infinite loop until the break
        # asks user the length of the password
        listOfApps: list[str] = []
        listOfApps.append("Password Generator-------1")
        listOfApps.append("Object Sorter------------2")
        listOfApps.append("Number Guesser-----------3")
        print(len(listOfApps))
        print("Select the application:")
        for app in listOfApps:
            print(app)
        user_input = input("> ")
        user_choice = ''.join(c for c in user_input if c.isnumeric())
        if len(user_choice) > 0:
            if 0 < int(user_choice) <= len(listOfApps):
                break  # break after there's a numeric & legit length

    user_choice = int(user_choice)
    match int(user_choice):
        case 1:
            password_gen_prompt()
        case 2:
            char_sorter_prompt()
        case 3:
            num_guesser_prompt()
