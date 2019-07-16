#
# @lc app=leetcode id=806 lang=python3
#
# [806] Number of Lines To Write String
#
class Solution:
    def numberOfLines(self, widths: List[int], S: str) -> List[int]:
        line = 1
        lsum = 0
        for i in range(0,len(S)):
            k = ord(S[i]) - 97
            if lsum <= 100 and lsum + widths[k] > 100:
                line = line + 1
                lsum = 0
            if lsum + widths[k] <= 100:
                lsum = lsum + widths[k]
        return [line,lsum]

