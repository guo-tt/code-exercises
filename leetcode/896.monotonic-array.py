#
# @lc app=leetcode id=896 lang=python3
#
# [896] Monotonic Array
#
class Solution:
    def isMonotonic(self, A):
        return self.increase(A) or self.decrease(A)
    
    def increase(self, A):
        return all(A[i] - A[i+1] <= 0 for i in range(0,len(A)-1))

    def decrease(self, A):
        return all(A[i] - A[i+1] >= 0 for i in range(0,len(A)-1))

