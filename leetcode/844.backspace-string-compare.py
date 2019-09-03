#
# @lc app=leetcode id=844 lang=python3
#
# [844] Backspace String Compare
#
class Solution:
    def backspaceCompare(self, S, T):
        ans_S = ""
        ans_T = ""
        for s in S:
            if s == '#':
                if ans_S:
                    ans_S = ans_S[:-1]
            else:
                ans_S += s
        for t in T:
            if t == '#':
                if ans_T:
                    ans_T = ans_T[:-1]
            else:
                ans_T += t
        return ans_S == ans_T
                    
        
