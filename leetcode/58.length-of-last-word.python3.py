#
# [58] Length of Last Word
#
# https://leetcode.com/problems/length-of-last-word/description/
#
# algorithms
# Easy (32.09%)
# Total Accepted:    199.8K
# Total Submissions: 622.5K
# Testcase Example:  '"Hello World"'
#
# Given a string s consists of upper/lower-case alphabets and empty space
# characters ' ', return the length of last word in the string.
# 
# If the last word does not exist, return 0.
# 
# Note: A word is defined as a character sequence consists of non-space
# characters only.
# 
# Example:
# 
# Input: "Hello World"
# Output: 5
# 
# 
#
class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        else:
            l = s.split()
            if len(l) > 0:
                return len(l[len(l)-1])
            else:
                return 0

if __name__ == "__main__":
    print(Solution().lengthOfLastWord(" "))
