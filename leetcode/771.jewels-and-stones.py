#
# @lc app=leetcode id=771 lang=python3
#
# [771] Jewels and Stones
#
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        j = 0 
        for i in range(0,len(S)):
            if S[i] in J:
                j = j + 1

        return j

