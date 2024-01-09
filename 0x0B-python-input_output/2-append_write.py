#!/usr/bin/python3
"""defining append_write function"""


def append_write(filename="", text=""):
    """Appends filename with utf-8"""
    with open(filename, mode='a', encoding='utf-8') as file:
        return file.write(text)
