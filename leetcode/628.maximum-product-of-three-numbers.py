#
# @lc app=leetcode id=628 lang=python3
#
# [628] Maximum Product of Three Numbers
#
class Solution:
    def maximumProduct(self, nums):
        nums.sort()
        right = nums[-3] * nums[-2] * nums[-1]
        left = nums[0] * nums[1] * nums[-1]
        return max(left, right)
        

