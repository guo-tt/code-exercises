#
# [217] Contains Duplicate
#
# https://leetcode.com/problems/contains-duplicate/description/
#
# algorithms
# Easy (47.97%)
# Total Accepted:    233.4K
# Total Submissions: 486.5K
# Testcase Example:  '[1,2,3,1]'
#
# Given an array of integers, find if the array contains any duplicates.
# 
# Your function should return true if any value appears at least twice in the
# array, and it should return false if every element is distinct.
# 
# Example 1:
# 
# 
# Input: [1,2,3,1]
# Output: true
# 
# Example 2:
# 
# 
# Input: [1,2,3,4]
# Output: false
# 
# Example 3:
# 
# 
# Input: [1,1,1,3,3,4,3,2,4,2]
# Output: true
# 
#
class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for i in range(0,len(nums)):
            print(nums[i])
            if nums[i] in nums[i+1,]:
                return True
        return False

if __name__ == '__main__':
    print(Solution().containsDuplicate([1,1,2,4,3]))
        
