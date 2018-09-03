#
# [367] Valid Perfect Square
#
# https://leetcode.com/problems/valid-perfect-square/description/
#
# algorithms
# Easy (38.85%)
# Total Accepted:    82.5K
# Total Submissions: 212.2K
# Testcase Example:  '16'
#
# Given a positive integer num, write a function which returns True if num is a
# perfect square else False.
# 
# Note: Do not use any built-in library function such as sqrt.
# 
# Example 1:
# 
# 
# 
# Input: 16
# Output: true
# 
# 
# 
# Example 2:
# 
# 
# Input: 14
# Output: false
# 
# 
# 
# 
#
class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1: return True

        left, right = 0, num
        while left <= right:
            mid = int((left + right) / 2)
            if mid * mid >= num:
                right = mid - 1
            else:
                left = mid + 1
        return left * left == num

if __name__ == "__main__":
    print(Solution().isPerfectSquare(16))