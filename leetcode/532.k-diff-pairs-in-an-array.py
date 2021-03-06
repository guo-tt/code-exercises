#
# @lc app=leetcode id=532 lang=python3
#
# [532] K-diff Pairs in an Array
#
import collections

class Solution:
    def findPairs(self, nums, k):
        res = 0
        if k < 0: return 0
        elif k == 0:
            count = collections.Counter(nums)
            for n, v in count.items():
                if v >= 2:
                    res += 1
            return res
        else:
            nums = set(nums)
            for num in nums:
                if num + k in nums:
                    res += 1
            return res


        

