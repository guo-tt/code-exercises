#
# [504] Base 7
#
# https://leetcode.com/problems/base-7/description/
#
# algorithms
# Easy (43.89%)
# Total Accepted:    32K
# Total Submissions: 72.9K
# Testcase Example:  '100'
#
# Given an integer, return its base 7 string representation.
# 
# Example 1:
# 
# Input: 100
# Output: "202"
# 
# 
# 
# Example 2:
# 
# Input: -7
# Output: "-10"
# 
# 
# 
# Note:
# The input will be in range of [-1e7, 1e7].
# 
#
class Solution:
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num==0:
            return "0"
        res=''
        n=abs(num)
        while n:
            res=str(n%7)+res
            n//=7
        return res if num>0 else '-'+res
