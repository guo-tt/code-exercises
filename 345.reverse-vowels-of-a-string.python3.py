#
# [345] Reverse Vowels of a String
#
# https://leetcode.com/problems/reverse-vowels-of-a-string/description/
#
# algorithms
# Easy (39.71%)
# Total Accepted:    119.1K
# Total Submissions: 299.8K
# Testcase Example:  '"hello"'
#
# Write a function that takes a string as input and reverse only the vowels of
# a string.
# 
# Example 1:
# 
# 
# Input: "hello"
# Output: "holle"
# 
# 
# 
# Example 2:
# 
# 
# Input: "leetcode"
# Output: "leotcede"
# 
# 
# Note:
# The vowels does not include the letter "y".
# 
# 
# 
#
class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = {"a","e","i","o","u","A","E","I","O","U"}
        sv = ""
        for i in range(0,len(s)):
            if s[i] in vowels:
                sv += s[i]
        
        vs = sv[::-1]

        j = 0
        news = ""
        for i in range(0,len(s)):
            if s[i] in vowels:
                news += vs[j]
                j += 1
            else:
                news += s[i]

        return news

if __name__ == "__main__":
    print(Solution().reverseVowels("leetcode"))
        
