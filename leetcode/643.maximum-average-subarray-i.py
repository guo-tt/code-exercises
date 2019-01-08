#
# @lc app=leetcode id=643 lang=python3
#
# [643] Maximum Average Subarray I
#
# https://leetcode.com/problems/maximum-average-subarray-i/description/
#
# algorithms
# Easy (38.48%)
# Total Accepted:    42.7K
# Total Submissions: 111.1K
# Testcase Example:  '[1,12,-5,-6,50,3]\n4'
#
# 
# Given an array consisting of n integers, find the contiguous subarray of
# given length k that has the maximum average value. And you need to output the
# maximum average value.
# 
# 
# Example 1:
# 
# Input: [1,12,-5,-6,50,3], k = 4
# Output: 12.75
# Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75
# 
# 
# 
# Note:
# 
# 1 k n 
# Elements of the given array will be in the range [-10,000, 10,000].
# 
# 
#
class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        # i = 0
        # max = -10000.0
        # while i < len(nums) and i + k <= len(nums):
        #     if sum(nums[i:i+k]) > max:
        #         max = sum(nums[i:i+k])
        #         print(i)
        #         print(max)
        #     i = i + 1
        # return max/k
        sum = 0.0
        maxsum = -100000.0
        for i in range(len(nums)):
            sum += nums[i]
            if i >= k:
                sum -= nums[i-k]
            if i >= k-1:
                maxsum = max(sum/k,maxsum)
        return maxsum
            
if __name__ == "__main__":
    print(Solution().findMaxAverage([1,12,-5,-6,50,3],4))
