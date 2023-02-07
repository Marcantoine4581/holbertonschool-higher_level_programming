#!/usr/bin/python3
"""function that reads a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """
    Args:
        filename (file): The file to read.
    """
    with open("my_file_0.txt") as f:
        for line in f:
            print(line, end="")
