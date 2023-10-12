#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_dict = dict(sorted(a_dictionary.items()))
    for item in sorted_dict:
        print("{}: {}".format(item, sorted_dict.get(item)))
