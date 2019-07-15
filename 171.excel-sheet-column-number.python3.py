#
# [171] Excel Sheet Column Number
#
# https://leetcode.com/problems/excel-sheet-column-number/description/
#
# algorithms
# Easy (49.19%)
# Total Accepted:    176.1K
# Total Submissions: 358K
# Testcase Example:  '"A"'
#
# Given a column title as appear in an Excel sheet, return its corresponding
# column number.
# 
# For example:
# 
# 
# ⁠   A -> 1
# ⁠   B -> 2
# ⁠   C -> 3
# ⁠   ...
# ⁠   Z -> 26
# ⁠   AA -> 27
# ⁠   AB -> 28 
# ⁠   ...
# 
# 
# Example 1:
# 
# 
# Input: "A"
# Output: 1
# 
# 
# Example 2:
# 
# 
# Input: "AB"
# Output: 28
# 
# 
# Example 3:
# 
# 
# Input: "ZY"
# Output: 701
# 
# 
#

class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        k = 0 
        sum = 0
        i = len(s) - 1
        while i >= 0:
            sum = sum + (ord(s[i])-64)*pow(26,k)
            k = k + 1
            i -= 1
        return sum


if __name__ == '__main__':
    print(Solution().titleToNumber("AB"))
        
