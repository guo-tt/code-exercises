#
# @lc app=leetcode id=784 lang=python3
#
# [784] Letter Case Permutation
#
class Solution:
    def letterCasePermutation(self, S):
        res = [""]
        for s in S:
            if s.isalpha():
                res = [word + j for word in res for j in [s.lower(), s.upper()]]
            else:
                res = [word + s for word in res]
        return res

