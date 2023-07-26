import random
import string


def password_gen_prompt():
    min_pw_length, max_pw_length = 8, 256

    while True:  # infinite loop until the break
        # asks user the length of the password
        print("Length of your password:")
        user_input = input("> ")
        pw_length = ''.join(c for c in user_input if c.isnumeric())
        if len(pw_length) > 0:
            if min_pw_length <= int(pw_length) <= max_pw_length:
                break  # break after there's a numeric & legit length
        print("ERROR: Please enter an integer between 5 and 80 (inclusive).")

    allowed_characters = string.digits + string.ascii_letters + string.punctuation
        #  Only letters(U and l), symbols and numbers allowed
        #  Can be changed by adding different default strings from string lib
    generated_password = ''.join(random.choice(allowed_characters) for _ in range(int(pw_length)))
        # The for here is a single-line for loop. _ basically means nothing.
        # range(int(pw_length)) is basically taking the user inputted value and generating a range.
        # For example, if the input value is 10, it will be a range of (10), which is range(0, 10), which is 0-9.
        # Range is iterable through an iterator, such as a for loop.
        # In this case, the loop will iterate through 0-9, which is 10 times, achieving what we want to do.

    # A weak-warning here that doesn't seem to have any issue. To-be further investigated.
    print("Your password is: " + generated_password)


if __name__ == '__main__':
    password_gen_prompt()
