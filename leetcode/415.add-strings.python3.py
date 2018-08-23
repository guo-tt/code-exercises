#
# [415] Add Strings
#
# https://leetcode.com/problems/add-strings/description/
#
# algorithms
# Easy (41.96%)
# Total Accepted:    65K
# Total Submissions: 155K
# Testcase Example:  '"0"\n"0"'
#
# Given two non-negative integers num1 and num2 represented as string, return
# the sum of num1 and num2.
# 
# Note:
# 
# The length of both num1 and num2 is < 5100.
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.
# You must not use any built-in BigInteger library or convert the inputs to
# integer directly.
# 
# 
#
class Solution:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # """ it0 = 0
        # for i in range(0,len(num1)):
        #     it0 += (ord(num1[i]) - 48) * pow(10, len(num1)-i-1)

        # it1 = 0
        # for j in range(0,len(num2)):
        #     it1 += (ord(num2[j]) - 48) * pow(10, len(num2)-j-1)

        # return str(it0 + it1) """

        i = len(num1) - 1
        j = len(num2) - 1
        result = ''
        carry = 0
        while i >= 0 or j >= 0:
            if i >= 0:
                carry += ord(num1[i]) - ord('0')
            if j >= 0:
                carry += ord(num2[j]) - ord('0')
            result += chr(carry % 10 + ord('0'))
            carry //= 10
            i -= 1
            j -= 1
        if carry == 1:
            result += '1'
        return result[::-1]

if __name__ == "__main__":
    print(Solution().addStrings("13","14"))
        
