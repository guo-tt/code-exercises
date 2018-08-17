#
# [349] Intersection of Two Arrays
#
# https://leetcode.com/problems/intersection-of-two-arrays/description/
#
# algorithms
# Easy (48.92%)
# Total Accepted:    149.2K
# Total Submissions: 304.8K
# Testcase Example:  '[1,2,2,1]\n[2,2]'
#
# Given two arrays, write a function to compute their intersection.
# 
# Example 1:
# 
# 
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]
# 
# 
# 
# Example 2:
# 
# 
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
# 
# 
# Note:
# 
# 
# Each element in the result must be unique.
# The result can be in any order.
# 
# 
# 
# 
#

from collections import defaultdict

class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        output = []
        if len(nums1) < len(nums2):
            for i in nums1:
                if i in nums2:
                    output.append(i)
        else:
            for j in nums2:
                if j in nums1:
                    output.append(j)

        return list(set(output)) 
