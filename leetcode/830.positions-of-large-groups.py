#
# @lc app=leetcode id=830 lang=python3
#
# [830] Positions of Large Groups
#
class Solution:
    def largeGroupPositions(self, S):
        j = -1
        d = ''
        ans = []
        for i, c in enumerate(S + '#'):
            if c != d:
                if i - j >= 3:
                    ans.append([j, i - 1])
                j = i
            d = c
        return ans
