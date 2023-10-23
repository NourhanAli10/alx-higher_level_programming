#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            if i >= len(my_list):
                raise IndexError
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                count += 1
        print("\nnb_print: {}".format(count))
    except IndexError:
        print("\nnb_print: {}".format(count))
        raise
    return count

