#
# [520] Detect Capital
#
# https://leetcode.com/problems/detect-capital/description/
#
# algorithms
# Easy (51.86%)
# Total Accepted:    70K
# Total Submissions: 135.1K
# Testcase Example:  '"USA"'
#
# 
# Given a word, you need to judge whether the usage of capitals in it is right
# or not.
# 
# 
# 
# We define the usage of capitals in a word to be right when one of the
# following cases holds:
# 
# All letters in this word are capitals, like "USA".
# All letters in this word are not capitals, like "leetcode".
# Only the first letter in this word is capital if it has more than one letter,
# like "Google".
# 
# Otherwise, we define that this word doesn't use capitals in a right way.
# 
# 
# 
# Example 1:
# 
# Input: "USA"
# Output: True
# 
# 
# 
# Example 2:
# 
# Input: "FlaG"
# Output: False
# 
# 
# 
# Note:
# The input will be a non-empty word consisting of uppercase and lowercase
# latin letters.
# 
#
class Solution:
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        FlagC = 0
        FlagS = 0
        Flag = 0
        for i in range(0,len(word)):
            if word[0].isupper():
                if word[i].isupper():
                    FlagC += 1
                if word[i].isupper() == 0:
                    FlagS += 1
            if word[i].isupper() == 0 and word[0].isupper() == 0:
                Flag += 1
            
        if FlagC == len(word) or FlagS == len(word) -1 or Flag == len(word):
            return True    
        else:
            return False

if __name__ == "__main__":
    print(Solution().detectCapitalUse("mL"))

        
