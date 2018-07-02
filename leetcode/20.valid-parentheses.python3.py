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
        n1 = s.find('{')
        n2 = s.find('}')
        n3 = s.find('[')
        n4 = s.find(']')
        n5 = s.find('(')
        n6 = s.find(')')
        print(n1)
        print(n2)
        print(n3)
        print(n4)
        print(n5)
        print(n6)
        if len(s) == 0:
            return True
        elif len(s)%2 != 0:
            return False
        else:
            if s.count('{') != s.count('}') or s.count('[') != s.count(']') or s.count('(') != s.count(')'):
                return False
            elif (n2 - n1 > 0 and ( n2 - n1 ) % 2 == 0) or (n4 - n3 > 0 and (n4 - n3) % 2 == 0) or (n6 - n5 > 0 and ( n6 - n5) % 2 == 0): 
                return False
            else:
                return True
        
if __name__ == '__main__':
    print(Solution().isValid("(([]){})"))