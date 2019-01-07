#
# @lc app=leetcode id=400 lang=python3
#
# [400] Nth Digit
#
# https://leetcode.com/problems/nth-digit/description/
#
# algorithms
# Easy (29.93%)
# Total Accepted:    42.8K
# Total Submissions: 143K
# Testcase Example:  '3'
#
# Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8,
# 9, 10, 11, ... 
# 
# Note:
# n is positive and will fit within the range of a 32-bit signed integer (n <
# 231).
# 
# 
# Example 1:
# 
# Input:
# 3
# 
# Output:
# 3
# 
# 
# 
# Example 2:
# 
# Input:
# 11
# 
# Output:
# 0
# 
# Explanation:
# The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0,
# which is part of the number 10.
# 
# 
#
class Solution:
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        _len = 1
        cnt = 9
        start = 1
        while n > _len * cnt:
            n -= _len * cnt
            _len += 1
            cnt *= 10
            start *= 10
        start = start + (n - 1) / _len
        return int(str(start)[(n - 1) % _len])

if __name__ == "__main__":
    print(Solution().findNthDigit(9))
