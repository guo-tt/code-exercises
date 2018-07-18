#
# [268] Missing Number
#
# https://leetcode.com/problems/missing-number/description/
#
# algorithms
# Easy (45.62%)
# Total Accepted:    188K
# Total Submissions: 412.1K
# Testcase Example:  '[3,0,1]'
#
# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find
# the one that is missing from the array.
# 
# Example 1:
# 
# 
# Input: [3,0,1]
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: [9,6,4,2,3,5,7,0,1]
# Output: 8
# 
# 
# Note:
# Your algorithm should run in linear runtime complexity. Could you implement
# it using only constant extra space complexity?
# 
#
class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # nums.sort()
        # if len(nums) > 1:
        #     if nums[0] != 0:
        #         return 0
        #     else:
        #         for i in range(0,len(nums)-1):
        #             if nums[i+1]-nums[i] != 1:
        #                 return nums[i]+1
        #         if i == len(nums)-2:
        #             return nums[len(nums)-1]+1
        # else:
        #     if nums[0] == 1:
        #         return 0
        #     if nums[0] == 0:
        #         return 1
        """
        :type nums: List[int]
        :rtype: int
        """
        temp_sum = len(nums)*(len(nums)+1)/2
        t_sum = sum(nums)
        return int(temp_sum - t_sum)

if __name__ == "__main__":
    print(Solution().missingNumber([0,1,2]))
        
