#
# @lc app=leetcode id=1018 lang=python3
#
# [1018] Binary Prefix Divisible By 5
#
class Solution:
    def prefixesDivBy5(self, A):
        res = []
        prefix = 0
        for a in A:
            prefix = (prefix * 2 + a) % 5
            res.append(prefix == 0)
        return res
        

