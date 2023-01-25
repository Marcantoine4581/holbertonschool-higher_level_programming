#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dictio = a_dictionary.copy()
    dictio.update((key, value * 2) for key, value in dictio.items())
    return dictio
