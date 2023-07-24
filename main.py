import random
import string
min_pw_length = 5

if __name__ == '__main__':
    while True:  # infinite loop until the break
        # asks user the length of the password
        print("Length of your password:")
        user_input = input("> ")
        pw_length = ''.join(c for c in user_input if c.isnumeric())
        if int(pw_length) > min_pw_length:
            break  # break after there's a numeric & legit length

    allowed_characters = string.ascii_letters + string.punctuation + string.digits
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
