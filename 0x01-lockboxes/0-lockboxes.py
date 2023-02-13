#!/usr/bin/python3
"""determine if all the boxes can be opened"""


def canUnlockAll(boxes):
    """
    Return: True or False
    """
    a = len(boxes)
    stack = [0]
    unlocked_box = [1] + [0] * (a - 1)
    i = 0

    if a == 0:
        return True
    while stack:
        j = stack.pop()
        for index in boxes[j]:
            if index > 0 and index < a and unlocked_box[index] == 0:
                unlocked_box[index] = 1
                stack.append(index)
        i = i + 1
    if 0 in unlocked_box:
        return False
    return True
