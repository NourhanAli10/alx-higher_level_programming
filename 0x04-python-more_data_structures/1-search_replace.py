#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    eleindex = new_list.index(search)
    new_list[eleindex] = replace
    return new_list
