#
# @lc app=leetcode id=796 lang=python3
#
# [796] Rotate String
#
class Solution:
    def rotateString(self, A: str, B: str):
        if len(A) != len(B):
            return False
        new = A + A
        if B in new:
            return True
        else:
            return False
        

