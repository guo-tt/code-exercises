#
# [67] Add Binary
#
# https://leetcode.com/problems/add-binary/description/
#
# algorithms
# Easy (34.84%)
# Total Accepted:    212.9K
# Total Submissions: 611K
# Testcase Example:  '"11"\n"1"'
#
# Given two binary strings, return their sum (also a binary string).
# 
# The input strings are both non-empty and contains only characters 1 or 0.
# 
# Example 1:
# 
# 
# Input: a = "11", b = "1"
# Output: "100"
# 
# Example 2:
# 
# 
# Input: a = "1010", b = "1011"
# Output: "10101"
# 
#
class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        l = max(len(a),len(b)) + 1
        a = a.zfill(l)
        b = b.zfill(l)
        c = "" 
        flag = 0

        while l > 0:
            if int(a[l-1]) + int(b[l-1]) + flag == 3:
                flag = 1
                c = "1" + c
            if int(a[l-1]) + int(b[l-1]) + flag == 2:
                flag = 1
                c = "0" + c
            if  int(a[l-1]) + int(b[l-1]) + flag <= 1:
                c = str(int(a[l-1]) + int(b[l-1]) + flag) + c
                flag = 0
            l -= 1

        if c[0] == "0" and c[1] == "0" and len(c) > 2:
           c = '1' + c[1:]
        if c[0] == "0":
           c = c[1:]
        return c
        
if __name__ == "__main__":
    print(Solution().addBinary("1111","1111"))