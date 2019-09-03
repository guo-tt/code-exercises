#
# [125] Valid Palindrome
#
# https://leetcode.com/problems/valid-palindrome/description/
#
# algorithms
# Easy (27.98%)
# Total Accepted:    249K
# Total Submissions: 890.1K
# Testcase Example:  '"A man, a plan, a canal: Panama"'
#
# Given a string, determine if it is a palindrome, considering only
# alphanumeric characters and ignoring cases.
# 
# Note: For the purpose of this problem, we define empty string as valid
# palindrome.
# 
# Example 1:
# 
# 
# Input: "A man, a plan, a canal: Panama"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: "race a car"
# Output: false
# 
# 
#
class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0:
            return True

        # ss = list(s.lower())    
        # ss = [i for i in ss if (ord(i) > 64 and ord(i) < 91) or (ord(i) > 96 and ord(i) < 123)]

        # i = len(ss)
        # sss = []
        # while i > 0:
        #     sss.append(ss[i-1])
        #     i -= 1

        # for i in range(0,len(ss)):
        #     if ss[i] != sss[i]:
        #         return False

        # return True
        alphanumericS = [c for c in s.lower() if c.isalnum()]
        return alphanumericS == alphanumericS[::-1]

if __name__ == '__main__':
    print(Solution().isPalindrome("0P"))
        
