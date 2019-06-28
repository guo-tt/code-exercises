#
# [387] First Unique Character in a String
#
# https://leetcode.com/problems/first-unique-character-in-a-string/description/
#
# algorithms
# Easy (47.33%)
# Total Accepted:    144.1K
# Total Submissions: 304.4K
# Testcase Example:  '"leetcode"'
#
# 
# Given a string, find the first non-repeating character in it and return it's
# index. If it doesn't exist, return -1.
# 
# Examples:
# 
# s = "leetcode"
# return 0.
# 
# s = "loveleetcode",
# return 2.
# 
# 
# 
# 
# Note: You may assume the string contain only lowercase letters.
# 
#
class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return -1
        elif len(s) == 1:
            return 0
        else:
            for i in range(0,len(s)):
                if s[i] not in s[i+1:] and s[i] not in s[:i]:
                    return i
            if i == len(s) - 1:
                return -1

if __name__ == "__main__":
    print(Solution().firstUniqChar('aadadaadi'))
