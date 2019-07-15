
#
# [20] Valid Parentheses
#
# https://leetcode.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (34.26%)
# Total Accepted:    355.6K
# Total Submissions: 1M
# Testcase Example:  '"()"'
#
# Given a string containing just the characters '(', ')', '{', '}', '[' and
# ']', determine if the input string is valid.
# 
# An input string is valid if:
# 
# 
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# 
# 
# Note that an empty string is also considered valid.
# 
# Example 1:
# 
# 
# Input: "()"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: "()[]{}"
# Output: true
# 
# 
# Example 3:
# 
# 
# Input: "(]"
# Output: false
# 
# 
# Example 4:
# 
# 
# Input: "([)]"
# Output: false
# 
# 
# Example 5:
# 
# 
# Input: "{[]}"
# Output: true
# 
# 
#

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        temp = []
        if len(s) == 0:
            return True
        elif s.count('[') != s.count(']') or s.count('{') != s.count('}') or s.count('(') != s.count(')'):
            return False
        else:
            for st in s:
                if st == "{" or st == "[" or st =="(":
                    temp.append(st)
                if st == "}" and temp[len(temp)-1] == "{":
                    temp.pop()
                if st == "]" and temp[len(temp)-1] == "[":
                    temp.pop()
                if st == ")" and temp[len(temp)-1] == "(":
                    temp.pop()
            if(len(temp) == 0):
                return True
            else:
                return False
                    
if __name__ == '__main__':
    print(Solution().isValid("]"))