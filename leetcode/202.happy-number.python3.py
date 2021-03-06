#
# [202] Happy Number
#
# https://leetcode.com/problems/happy-number/description/
#
# algorithms
# Easy (42.28%)
# Total Accepted:    173.4K
# Total Submissions: 410.1K
# Testcase Example:  '19'
#
# Write an algorithm to determine if a number is "happy".
# 
# A happy number is a number defined by the following process: Starting with
# any positive integer, replace the number by the sum of the squares of its
# digits, and repeat the process until the number equals 1 (where it will
# stay), or it loops endlessly in a cycle which does not include 1. Those
# numbers for which this process ends in 1 are happy numbers.
# 
# Example: 
# 
# 
# Input: 19
# Output: true
# Explanation: 
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1
# 
# 
#
class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        res = 0
        while n:
            res = res + (n % 10)**2
            n = int(n/10)
        n = res    
        if n > 4:
           return self.isHappy(n)
        else:
           return n == 1

if __name__ == "__main__":
    print(Solution().isHappy(19))
