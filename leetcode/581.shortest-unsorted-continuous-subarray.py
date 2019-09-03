#
# @lc app=leetcode id=581 lang=python3
#
# [581] Shortest Unsorted Continuous Subarray
#
class Solution:
    def findUnsortedSubarray(self, nums):
        snum = nums.copy()
        snum.sort()
        i = 0
        while i < len(nums):
            if snum[i] != nums[i]:
                f = i
                break 
            i = i + 1  
        
        j = len(nums) - 1 
        while j > 0:
            if snum[j] != nums[j]:
                e = j 
                break 
            j = j - 1 

        if j - i > 0: 
            return j - i + 1
        else:
            return 0

