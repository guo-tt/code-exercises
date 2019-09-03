#
# @lc app=leetcode id=944 lang=python3
#
# [944] Delete Columns to Make Sorted
#
class Solution:
    def minDeletionSize(self, A):
        res = 0
        N = len(A[0])
        for i in range(N):
            col = [a[i] for a in A]
            if col != sorted(col):
                res += 1
        return res
        

