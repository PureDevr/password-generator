import string


def char_sorter_prompt():
    while True:
        print("Insert a string of random characters:")
        unsorted_str = input("> ")
        if len(unsorted_str) >= 2:
            break
        print("ERROR: Please insert at least 2 characters.")

    allowed_char = string.digits + string.ascii_uppercase + string.ascii_lowercase + string.punctuation

    occurrences = [0] * len(allowed_char)

    # Why for loop on allowed_char first?
    for i_allowed, c_allowed in enumerate(allowed_char):  # c stands for currently-iterating element, i for index
        for c_unsorted in unsorted_str:
            if c_unsorted == c_allowed:
                occurrences[i_allowed] += 1

    sorted_str = ''
    # for i_allowed, c_allowed in enumerate(allowed_char):
    #     for _ in range(occurrences[i_allowed]):
    #         sorted_str += c_allowed

    for i_occurrences, c_occurrences in enumerate(occurrences):
        for _ in range(c_occurrences):
            sorted_str += allowed_char[i_occurrences]

    # print(occurrences)
    print(sorted_str)
    # print("test")


if __name__ == '__main__':
    char_sorter_prompt()
