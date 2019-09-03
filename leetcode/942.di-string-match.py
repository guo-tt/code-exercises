#
# @lc app=leetcode id=942 lang=python3
#
# [942] DI String Match
#
class Solution:
    def diStringMatch(self, S):
       ni, nd = 0, len(S)
       res = []
       for s in S:
           if s == "I":
               res.append(ni)
               ni = ni + 1
           if s == "D":
               res.append(nd)
               nd = nd - 1
       res.append(ni)
       return res

