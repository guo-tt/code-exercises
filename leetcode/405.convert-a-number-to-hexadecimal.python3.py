#
# [405] Convert a Number to Hexadecimal
#
# https://leetcode.com/problems/convert-a-number-to-hexadecimal/description/
#
# algorithms
# Easy (41.19%)
# Total Accepted:    37.4K
# Total Submissions: 90.7K
# Testcase Example:  '26'
#
# 
# Given an integer, write an algorithm to convert it to hexadecimal. For
# negative integer, two’s complement method is used.
# 
# 
# Note:
# 
# All letters in hexadecimal (a-f) must be in lowercase.
# The hexadecimal string must not contain extra leading 0s. If the number is
# zero, it is represented by a single zero character '0'; otherwise, the first
# character in the hexadecimal string will not be the zero character.
# The given number is guaranteed to fit within the range of a 32-bit signed
# integer.
# You must not use any method provided by the library which converts/formats
# the number to hex directly.
# 
# 
# 
# Example 1:
# 
# Input:
# 26
# 
# Output:
# "1a"
# 
# 
# 
# Example 2:
# 
# Input:
# -1
# 
# Output:
# "ffffffff"
# 
# 
#
class Solution:
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        dict = {10:"a",11:"b",12:"c",13:"d",14:"e",15:"f"}
        output = ""
        if num < 0:
            num += 2**32

        if num > 0 and num < 10:
            return str(num)
        elif num >=10 and num < 16:
            return dict[num]

        while num >= 16:
            num, m = divmod(num, 16)
            if m in dict:
                output = dict[m] + output
            else:
                output = str(m) + output

        if num in dict: 
            output = dict[num] + output
        else:
            output = str(num) + output
            
        return output
        # s = ''
        # s1 = []
        # if num > 0 and num < 10:
        #     return str(num)
        # elif num >=10 and num < 16:
        #     return dict[num]

        # while num >= 16:
        #     num, res =divmod(num, 16)
        #     s1.append(res)
        # s1.append(num)
        # for i in s1:
        #     if i < 10:
        #         s = str(i) + s
        #     else:
        #         s = dict[i] + s
        # return s

if __name__ == "__main__":
    print(Solution().toHex(-2))
            



        
