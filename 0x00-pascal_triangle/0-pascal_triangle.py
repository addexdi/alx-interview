#!/usr/bin/python3
'''
    list of lists representing the pascal triangle
'''


def pascal_triangle(n):
    '''
        returns a list of lists
    '''
    pascal = []
    if type(n) is not int or n <= 0:
        return []
    if n > 0 and n <= 5:
        for i in range(n):
            if i < 5:
                pascal.append(list(map(int, list(str(11**i)))))
    if n > 5:
        for i in range(n):
            attach = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    attach.append(1)
                elif i > 0 and j > 0:
                    attach.append(pascal[i - 1][j - 1] + pascal[i - 1][j])
            pascal.append(attach)
    return pascal
