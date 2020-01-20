#
# @lc app=leetcode id=1189 lang=python3
#
# [1189] Maximum Number of Balloons
#
from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text):
        cnt = Counter(text)
        return min(cnt['b'], cnt['a'], cnt['l']//2, cnt['o']//2, cnt['n'])

        

