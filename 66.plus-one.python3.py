#
# [66] Plus One
#
# https://leetcode.com/problems/plus-one/description/
#
# algorithms
# Easy (39.88%)
# Total Accepted:    260.8K
# Total Submissions: 653.9K
# Testcase Example:  '[1,2,3]'
#
# Given a non-empty array of digits representing a non-negative integer, plus
# one to the integer.
# 
# The digits are stored such that the most significant digit is at the head of
# the list, and each element in the array contain a single digit.
# 
# You may assume the integer does not contain any leading zero, except the
# number 0 itself.
# 
# Example 1:
# 
# 
# Input: [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# 
# 
# Example 2:
# 
# 
# Input: [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# 
# 
#
class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        flag = 0
        i = len(digits)
        if i == 0:
            return 0
        else:
            while i > 0:
                if digits[i-1] + 1 < 10:
                    digits[i-1] += 1
                    return digits
                else:
                    digits[i-1] = 0
                    flag = 1
                if flag == 1:
                    i -= 1
            if i == 0:
                digits = [1] + digits 
            return digits

print(Solution().plusOne([1,9,9,9]))
        
