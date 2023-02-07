#!/usr/bin/python3
"""function that reads a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """
    Args:
        filename (file): The file to read.
    """
    with open("my_file_0.txt", encoding="utf-8") as f:
        print(f.read(), end="")

