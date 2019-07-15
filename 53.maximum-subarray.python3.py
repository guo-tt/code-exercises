#
# [53] Maximum Subarray
#
# https://leetcode.com/problems/maximum-subarray/description/
#
# algorithms
# Easy (40.71%)
# Total Accepted:    331K
# Total Submissions: 813.1K
# Testcase Example:  '[-2,1,-3,4,-1,2,1,-5,4]'
#
# Given an integer array nums, find the contiguous subarray (containing at
# least one number) which has the largest sum and return its sum.
# 
# Example:
# 
# 
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# 
# 
# Follow up:
# 
# If you have figured out the O(n) solution, try coding another solution using
# the divide and conquer approach, which is more subtle.
# 
#
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        thisSum = 0
        maxSum = -100000000000
        for i in nums:
            if thisSum < 0:
                thisSum = 0
            thisSum += i
            if thisSum > maxSum:
                maxSum = thisSum

        return maxSum
        
if __name__ == '__main__':
    print(Solution().maxSubArray([4,-1,2,1]))