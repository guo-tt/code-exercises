#
# [168] Excel Sheet Column Title
#
# https://leetcode.com/problems/excel-sheet-column-title/description/
#
# algorithms
# Easy (27.68%)
# Total Accepted:    142.4K
# Total Submissions: 514.6K
# Testcase Example:  '1'
#
# Given a positive integer, return its corresponding column title as appear in
# an Excel sheet.
# 
# For example:
# 
# 
# ⁠   1 -> A
# ⁠   2 -> B
# ⁠   3 -> C
# ⁠   ...
# ⁠   26 -> Z
# ⁠   27 -> AA
# ⁠   28 -> AB 
# ⁠   ...
# 
# 
# Example 1:
# 
# 
# Input: 1
# Output: "A"
# 
# 
# Example 2:
# 
# 
# Input: 28
# Output: "AB"
# 
# 
# Example 3:
# 
# 
# Input: 701
# Output: "ZY"
# 
# 
#
class Solution:
    def convertToTitle(self, n):    
        """
        :type n: int
        :rtype: str
        """
        res = ''
        while n:
            res = chr((n-1)%26 + 65) + res
            print(res)
            print(n)
            n = int((n-1) / 26)
        return res        

if __name__ == '__main__':
    print(Solution().convertToTitle(701))
        
