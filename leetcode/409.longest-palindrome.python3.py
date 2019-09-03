#
# [409] Longest Palindrome
#
# https://leetcode.com/problems/longest-palindrome/description/
#
# algorithms
# Easy (46.28%)
# Total Accepted:    71.7K
# Total Submissions: 155K
# Testcase Example:  '"abccccdd"'
#
# Given a string which consists of lowercase or uppercase letters, find the
# length of the longest palindromes that can be built with those letters.
# 
# This is case sensitive, for example "Aa" is not considered a palindrome
# here.
# 
# Note:
# Assume the length of given string will not exceed 1,010.
# 
# 
# Example: 
# 
# Input:
# "abccccdd"
# 
# Output:
# 7
# 
# Explanation:
# One longest palindrome that can be built is "dccaccd", whose length is 7.
# 
# 
#
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        dicts = {}
        for i in s:
            if i not in dicts:
                dicts[i] = 1
            else:
                dicts[i] += 1

        ans = odd = 0
        for c in dicts:
            ans += dicts[c]
            if dicts[c] % 2 == 1:
                ans -= 1
                odd += 1
        return ans + (odd > 0)
    
if __name__ == "__main__":
    print(Solution().longestPalindrome("abccccdd"))
