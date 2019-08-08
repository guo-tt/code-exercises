#
# @lc app=leetcode id=724 lang=python3
#
# [724] Find Pivot Index
#
class Solution:
    def pivotIndex(self, nums):
        if len(nums) == 0:
            return -1
        
        left = 0
        right = sum(nums)
        for i in range(len(nums)):
            if i != 0:
                left += nums[i - 1]
            right -= nums[i]
            if left == right:
                return i
        return -1
    
