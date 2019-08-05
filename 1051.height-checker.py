#
# @lc app=leetcode id=1051 lang=python3
#
# [1051] Height Checker
#
class Solution:
    def heightChecker(self, heights):
        sorted_heights = sorted(heights)
        res = 0
        for v1,v2 in zip(heights,sorted_heights):
            res += 1 if v1 != v2 else  0
        return res

        

