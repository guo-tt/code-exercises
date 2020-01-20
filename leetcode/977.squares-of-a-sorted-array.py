#
# @lc app=leetcode id=977 lang=python3
#
# [977] Squares of a Sorted Array
#
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        return sorted([_ ** 2 for _ in A])
        

