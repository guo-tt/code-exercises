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
        m = 0
        n = 0
        rep = 0
        k = 0
        if len(A) != len(B):
            return False
        else:
            for i in range(0,len(A)):
                if A[i] in A[i+1:]:
                    rep = 1
                if A[i] == B[i]:
                    k += 1
                else:
                    if m == 0:
                        m = i
                    else:
                        n = i

            if k == len(A) - 2 and A[m] == B[n]:
                return True 
            elif k == len(A) and rep == 1:
                return True
            else:
                return False

if __name__ == "__main__":
    print(Solution().buddyStrings("ab","ba"))
        
