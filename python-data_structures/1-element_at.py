#!/usr/bin/python3
def element_at(my_list, idx):
    index = 0
    for i in my_list:
        if index == idx:
            return(i)
        index += 1
