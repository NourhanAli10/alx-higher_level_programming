#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        element = "None"
    elif idx > len(my_list) - 1:
        element = "None"
    else:
        element = my_list.pop(idx)
    return (element)
