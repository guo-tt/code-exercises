#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#
import collections

class Solution:
    def isSubsequence(self, s, t):
        queue = collections.deque(s)
        for c in t:
            if not queue: return True
            if c == queue[0]:
                queue.popleft()
        return not queue



        

