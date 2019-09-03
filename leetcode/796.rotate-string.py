#
# @lc app=leetcode id=796 lang=python3
#
# [796] Rotate String
#
class Solution:
    def rotateString(self, A, B):
        if len(A) != len(B):
            return False
        S = A + A  
        return B in S
        

