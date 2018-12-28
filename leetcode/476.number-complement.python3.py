#
# [476] Number Complement
#
# https://leetcode.com/problems/number-complement/description/
#
# algorithms
# Easy (61.36%)
# Total Accepted:    88.4K
# Total Submissions: 144.1K
# Testcase Example:  '5'
#
# Given a positive integer, output its complement number. The complement
# strategy is to flip the bits of its binary representation.
# 
# Note:
# 
# The given integer is guaranteed to fit within the range of a 32-bit signed
# integer.
# You could assume no leading zero bit in the integer’s binary
# representation.
# 
# 
# 
# Example 1:
# 
# Input: 5
# Output: 2
# Explanation: The binary representation of 5 is 101 (no leading zero bits),
# and its complement is 010. So you need to output 2.
# 
# 
# 
# Example 2:
# 
# Input: 1
# Output: 0
# Explanation: The binary representation of 1 is 1 (no leading zero bits), and
# its complement is 0. So you need to output 0.
# 
# 
#
class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        s=""
        while num > 0:
            s = str(num % 2) + s
            num = num // 2

        o = 0
        for i in range(0,len(s)):
            if s[i] == "0":
                o += pow(2,len(s)-i-1)
            
        return o

if __name__ == "__main__":
    print(Solution().findComplement(2))
