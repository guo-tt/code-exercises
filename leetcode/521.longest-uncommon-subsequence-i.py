#
# @lc app=leetcode id=521 lang=python3
#
# [521] Longest Uncommon Subsequence I 
#
class Solution:
    def findLUSlength(self, a, b):
        return max(len(a), len(b)) if a != b else -1
        

