#
# [633] Sum of Square Numbers
#
# https://leetcode.com/problems/sum-of-square-numbers/description/
#
# algorithms
# Easy (32.36%)
# Total Accepted:    32.3K
# Total Submissions: 99.9K
# Testcase Example:  '5'
#
# 
# Given a non-negative integer c, your task is to decide whether there're two
# integers a and b such that a2 + b2 = c.
# 
# 
# Example 1:
# 
# Input: 5
# Output: True
# Explanation: 1 * 1 + 2 * 2 = 5
# 
# 
# 
# 
# Example 2:
# 
# Input: 3
# Output: False
# 
# 
# 
#
import math

class Solution:
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        for i in range(0,int(math.sqrt(c)+1)):
            j = c - i*i
            if((int(j**0.5)**2)==j):
                return True
        return False

if __name__ == '__main__':
    print(Solution().judgeSquareSum(0))