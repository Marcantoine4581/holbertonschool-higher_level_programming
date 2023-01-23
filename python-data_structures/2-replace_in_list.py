#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    index = 0
    if idx >= (len(my_list) - 1):
        return(my_list)
    for i in my_list:
        if index == idx:
            my_list[idx] = element
            return(my_list)
        index += 1
