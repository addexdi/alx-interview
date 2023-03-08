#!/usr/bin/python3
""" Prime Game function """


def isWinner(x, nums):
    """ Maria and Ben are playing a game. Given a set of consecutive
    integers starting from 1 up to and including n,
    they take turns choosing a prime number from the set and
    removing that number and its multiples from the set.
    The player that cannot make a move loses the game.
    They play x rounds of the game, where n may be different for each
    round. Assuming Maria always goes first and both players play optimally,
    determine who the winner of each game is"""
    if not nums or x < 1:
        return None
    n = max(nums)
    fltr = [True for _ in range(max(n + 1, 2))]
    for i in range(2, int(pow(n, 0.5)) + 1):
        if not fltr[i]:
            continue
        for j in range(i * i, n + 1, i):
            fltr[j] = False
    fltr[0] = fltr[1] = False
    c = 0
    for i in range(len(fltr)):
        if fltr[i]:
            c += 1
        fltr[i] = c
    plyr1 = 0
    for n in nums:
        plyr1 += fltr[n] % 2 == 1
    if plyr1 * 2 == len(nums):
        return None
    if plyr1 * 2 > len(nums):
        return "Maria"
    return "Ben"
