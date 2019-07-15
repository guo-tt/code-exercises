#
# [953] Reverse Only Letters
#
# https://leetcode.com/problems/reverse-only-letters/description/
#
# algorithms
# Easy (58.01%)
# Total Accepted:    6.4K
# Total Submissions: 11.1K
# Testcase Example:  '"ab-cd"'
#
# Given a string S, return the "reversed" string where all characters that are
# not a letter stay in the same place, and all letters reverse their
# positions.
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: "ab-cd"
# Output: "dc-ba"
# 
# 
# 
# Example 2:
# 
# 
# Input: "a-bC-dEf-ghIj"
# Output: "j-Ih-gfE-dCba"
# 
# 
# 
# Example 3:
# 
# 
# Input: "Test1ng-Leet=code-Q!"
# Output: "Qedo1ct-eeLg=ntse-T!"
# 
# 
# 
# 
# 
# Note:
# 
# 
# S.length <= 100
# 33 <= S[i].ASCIIcode <= 122 
# S doesn't contain \ or "
# 
# 
# 
# 
# 
# 
#
class Solution:
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        # strss = ""
        # chr_dic = dict()
        # for i in range(0,len(S)):
        #     if (S[i] >= "a" and S[i] <= "z") or (S[i] >= "A" and S[i] <= "Z"):
        #         strss = strss + S[i]
        #     else:
        #         chr_dic[i] = S[i]

        # rstrss = ""
        # i = len(strss) - 1
        # while i >= 0:
        #     rstrss = rstrss + strss[i]
        #     i = i - 1

        # otrss = ""
        # j = 0
        # for i in range(0,len(S)):
        #     if i not in chr_dic:
        #         otrss = otrss + rstrss[j]
        #         j = j + 1
        #     else:
        #         otrss = otrss + chr_dic[i]

        # return otrss

        p = [i for i in S if i.isalpha()]
        return ''.join([i if not i.isalpha() else p.pop() for i in S])

if __name__ == "__main__":
    print(Solution().reverseOnlyLetters("Test1ng-Leet=code-Q!"))