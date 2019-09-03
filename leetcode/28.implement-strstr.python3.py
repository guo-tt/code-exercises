#
# [28] Implement strStr()
#
# https://leetcode.com/problems/implement-strstr/description/
#
# algorithms
# Easy (29.40%)
# Total Accepted:    287.9K
# Total Submissions: 979.3K
# Testcase Example:  '"hello"\n"ll"'
#
# Implement strStr().
# 
# Return the index of the first occurrence of needle in haystack, or -1 if
# needle is not part of haystack.
# 
# Example 1:
# 
# 
# Input: haystack = "hello", needle = "ll"
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: haystack = "aaaaa", needle = "bba"
# Output: -1
# 
# 
# Clarification:
# 
# What should we return when needle is an empty string? This is a great
# question to ask during an interview.
# 
# For the purpose of this problem, we will return 0 when needle is an empty
# string. This is consistent to C's strstr() and Java's indexOf().
# 
#
class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        flag = 1
        if len(needle) == 0:
            return 0
        if len(haystack) == 0:
            return -1
        for i in range(len(haystack)):
            if i + len(needle) > len(haystack):
                return -1
            else:
                if haystack[i:i+len(needle)] == needle:
                    return i
                else:
                    flag *= 0
        if flag == 0:
            return -1        

if __name__ == "__main__":
    print(Solution().strStr("mississipi","a"))