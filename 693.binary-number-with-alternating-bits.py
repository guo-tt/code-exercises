#
# @lc app=leetcode id=693 lang=python3
#
# [693] Binary Number with Alternating Bits
#
class Solution:
    def hasAlternatingBits(self, n):
        while n:
           a = n%2
           n = int(n/2)
           if a%2 == 0 and n%2 == 0:
               return False
           if a%2 == 1 and n%2 == 1:
               return False
        return True

