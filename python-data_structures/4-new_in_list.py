#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    index = 0
    if idx < 0 or idx > (len(my_list) - 1):
        return(my_list)
    index = 0
    new_list = my_list.copy()
    for i in new_list:
        if index == idx:
            new_list[idx] = element
            return(new_list)
        index += 1
