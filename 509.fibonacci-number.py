#
# @lc app=leetcode id=509 lang=python3
#
# [509] Fibonacci Number
#
class Solution:
    def fib(self, N):
        if N <= 1:
            return N
        return self.fib(N-1) + self.fib(N-2)
        
