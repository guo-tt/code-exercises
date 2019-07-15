#
# [459] Repeated Substring Pattern
#
# https://leetcode.com/problems/repeated-substring-pattern/description/
#
# algorithms
# Easy (38.50%)
# Total Accepted:    59.5K
# Total Submissions: 154.5K
# Testcase Example:  '"abab"'
#
# Given a non-empty string check if it can be constructed by taking a substring
# of it and appending multiple copies of the substring together. You may assume
# the given string consists of lowercase English letters only and its length
# will not exceed 10000.
# 
# 
# 
# Example 1:
# 
# 
# Input: "abab"
# Output: True
# Explanation: It's the substring "ab" twice.
# 
# 
# Example 2:
# 
# 
# Input: "aba"
# Output: False
# 
# 
# Example 3:
# 
# 
# Input: "abcabcabcabc"
# Output: True
# Explanation: It's the substring "abc" four times. (And the substring "abcabc"
# twice.)
# 
# 
#
class Solution:
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # i = 1
        # while i < len(s):
        #     subS =  s[:i]
        #     k = 2 
        #     while len(subS) * k <= len(s):
        #         if subS * k == s:
        #             return True
        #         k += 1
        #     i += 1
            
        # return False
        return s in s[1:] + s[:-1]
        
if __name__ == "__main__":
    print(Solution().repeatedSubstringPattern("babbabbabbabbab"))

