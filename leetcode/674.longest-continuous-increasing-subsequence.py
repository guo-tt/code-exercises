#
# @lc app=leetcode id=674 lang=python3
#
# [674] Longest Continuous Increasing Subsequence
#
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        l = 0
        i = 1
        maxl = 0
        while i < len(nums):
            if nums[i] - nums[i-1] > 0:
                l = l + 1
                i = i + 1
            else:
                maxl = max(maxl, l + 1)
                l = 0
                i = i + 1
        return max(maxl, l + 1)
            
