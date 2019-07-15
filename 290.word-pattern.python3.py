#
# [290] Word Pattern
#
# https://leetcode.com/problems/word-pattern/description/
#
# algorithms
# Easy (33.72%)
# Total Accepted:    109.9K
# Total Submissions: 326K
# Testcase Example:  '"abba"\n"dog cat cat dog"'
#
# Given a pattern and a string str, find if str follows the same pattern.
# 
# Here follow means a full match, such that there is a bijection between a
# letter in pattern and a non-empty word in str.
# 
# Example 1:
# 
# 
# Input: pattern = "abba", str = "dog cat cat dog"
# Output: true
# 
# Example 2:
# 
# 
# Input:pattern = "abba", str = "dog cat cat fish"
# Output: false
# 
# Example 3:
# 
# 
# Input: pattern = "aaaa", str = "dog cat cat dog"
# Output: false
# 
# Example 4:
# 
# 
# Input: pattern = "abba", str = "dog dog dog dog"
# Output: false
# 
# Notes:
# You may assume pattern contains only lowercase letters, and str contains
# lowercase letters separated by a single space.
# 
#
class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        d = {}
        str = str.split(" ")
        if len(pattern) != len(str):
            return False
        else:
            for i in range(0,len(pattern)):
                if pattern[i] not in d.keys() and str[i] not in d.values():
                    d[pattern[i]] = str[i]
                if pattern[i] not in d.keys() and str[i] in d.values():
                    return False
                if pattern[i] in d.keys() and str[i] not in d.values():
                    return False
                if pattern[i] in d.keys() and str[i] in d.values() and d[pattern[i]] != str[i]:
                    return False
            return True

if __name__ == '__main__':
    print(Solution().wordPattern("aba","dog cat cat"))