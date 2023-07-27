import random


def num_guesser_prompt():
    print("The system will generate a random integer between 0-999.")
    print("Guess an integer, the system will tell if the number is:\nHIGHER / LOWER / CORRECT")
    print("You will have 7 guesses.")
    min_number, max_number = 0, 999
    number = random.randint(min_number, max_number)
    # print(number)

    for i in range(7):
        while True:
            print("Enter your guess:")
            user_input = input("> ")
            user_guess = ''.join(c for c in user_input if c.isnumeric())
            if min_number <= int(user_guess) <= max_number:
                break
            print("ERROR: Input must be integer between 0-999.")
        if int(user_guess) < number:
            print("HIGHER!")
        elif int(user_guess) > number:
            print("LOWER!")
        else:
            print("CORRECT!\n")
            return
    print("You lost! The number is: " + str(number) + "\n")
# TBA: HOW MANY CHANCES LEFT.


if __name__ == '__main__':
    num_guesser_prompt()
