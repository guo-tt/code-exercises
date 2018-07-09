#
# [889] Buddy Strings
#
# https://leetcode.com/problems/buddy-strings/description/
#
# algorithms
# Easy (26.25%)
# Total Accepted:    5.8K
# Total Submissions: 22.1K
# Testcase Example:  '"ab"\n"ba"'
#
# Given two strings A and B of lowercase letters, return true if and only if we
# can swap two letters in A so that the result equals B.
# 
# 
# 
# Example 1:
# 
# 
# 
# Input: A = "ab", B = "ba"
# Output: true
# 
# 
# 
# Example 2:
# 
# 
# Input: A = "ab", B = "ab"
# Output: false
# 
# 
# 
# Example 3:
# 
# 
# Input: A = "aa", B = "aa"
# Output: true
# 
# 
# 
# Example 4:
# 
# 
# Input: A = "aaaaaaabc", B = "aaaaaaacb"
# Output: true
# 
# 
# 
# Example 5:
# 
# 
# Input: A = "", B = "aa"
# Output: false
# 
# 
# 
# 
# Note:
# 
# 
# 0 <= A.length <= 20000
# 0 <= B.length <= 20000
# A and B consist only of lowercase letters.
# 
# 
# 
# 
# 
# 
# 
#
class Solution:
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        k = 1
        i = 0
        if len(A) != len(B) or len(A) == 1 or len(B) == 1:
            return False
        elif len(A) == 0 or len(B) == 0:
            return False
        elif len(A) == 2 and len(B) == 2:
            if A[0] == B[1] and A[1] == B[0]:
                return True
            else:
                return False
        else:
            while i < len(A)-1:
                if A[i] == B[i]:
                    k += 1
                else:
                    if A[i] == B[i+1] and A[i+1] == B[i]:
                        i += 1 
                    else:
                        return False 
                i += 1

            if k == len(A):
                return False 
            else:
                return True 

if __name__ == "__main__":
    print(Solution().buddyStrings("abab","abab"))
        
