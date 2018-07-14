#
# [258] Add Digits
#
# https://leetcode.com/problems/add-digits/description/
#
# algorithms
# Easy (52.23%)
# Total Accepted:    203.9K
# Total Submissions: 390.4K
# Testcase Example:  '38'
#
# Given a non-negative integer num, repeatedly add all its digits until the
# result has only one digit.
# 
# Example:
# 
# 
# Input: 38
# Output: 2 
# Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. 
# Since 2 has only one digit, return it.
# 
# 
# Follow up:
# Could you do it without any loop/recursion in O(1) runtime?
# 
#
class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        # sum = 0
        # while(num/10 >= 1):
        #     sum += int(num%10)
        #     num = int(num/10)
        # sum = sum + num
        # num = sum
        # if num/10 < 1:
        #     return num
        # else:    
        #     return self.addDigits(num)
        if num == 0:
            return 0
        else:
            return 1 + (num - 1) % 9

if __name__ == '__main__':
    print(Solution().addDigits(38))
        
