#
# [686] Repeated String Match
#
# https://leetcode.com/problems/repeated-string-match/description/
#
# algorithms
# Easy (31.37%)
# Total Accepted:    46.4K
# Total Submissions: 147.9K
# Testcase Example:  '"abcd"\n"cdabcdab"'
#
# Given two strings A and B, find the minimum number of times A has to be
# repeated such that B is a substring of it. If no such solution, return -1.
# 
# For example, with A = "abcd" and B = "cdabcdab".
# 
# Return 3, because by repeating A three times (“abcdabcdabcd”), B is a
# substring of it; and B is not a substring of A repeated two times
# ("abcdabcd").
# 
# Note:
# The length of A and B will be between 1 and 10000.
# 
#
class Solution:
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        la = len(A)
        lb = len(B)

        n = 1
        s = ""
        if la <= lb:
            while n*la <= 3*lb:
                s = s + A
                if B in s:
                    return n
                else:
                    n += 1
            return -1
        else:
            if B in A:
                return 1
            elif B in A+A:
                return 2
            else:
                return -1
        
if __name__ == "__main__":
    print(Solution().repeatedStringMatch("abcd","bc"))
