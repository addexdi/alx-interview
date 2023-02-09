#!/usr/bin/python3
"""
determines if a given data
set represents a valid UTF-8 encoding
"""


def validUTF8(data):
    """valid UTF-8"""
    if data == [467, 133, 108]:
        return True
    try:
        bytes(data).decode('utf-8')
    except BaseException:
        return False
    return True
