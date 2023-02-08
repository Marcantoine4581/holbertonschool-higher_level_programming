#!/usr/bin/python3
"""function that writes a string to a text file (UTF8) and
returns the number of characters written"""


def write_file(filename="", text=""):
    """
    Args:
        filename (file): The file.
        text (str) : The text to write.
    Return:
        the number of characters written.
    """
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(text)
        return len(text)
