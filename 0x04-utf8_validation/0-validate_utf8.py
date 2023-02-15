#!/usr/bin/python3
""" UTF-8 encoding validator """


def validUTF8(data):
    """
    determines if a given data set represents a valid UTF-8 encoding

    Argument:
    data: list of integers
    """
    count = 0

    for bit in data:
        bin_data = bin(bit).replace('0b', '').rjust(8, '0')[-8:]
        if count == 0:
            if bin_data.startswith('110'):
                count = 1
            if bin_data.startswith('1110'):
                count = 2
            if bin_data.startswith('11110'):
                count = 3
            if bin_data.startswith('10'):
                return False
        else:
            if not bin_data.startswith('10'):
                return False
            count -= 1

    if count != 0:
        return False

    return True
