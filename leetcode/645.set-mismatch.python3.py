#
# [645] Set Mismatch
#
# https://leetcode.com/problems/set-mismatch/description/
#
# algorithms
# Easy (39.83%)
# Total Accepted:    35.5K
# Total Submissions: 89K
# Testcase Example:  '[1,2,2,4]'
#
# 
# The set S originally contains numbers from 1 to n. But unfortunately, due to
# the data error, one of the numbers in the set got duplicated to another
# number in the set, which results in repetition of one number and loss of
# another number. 
# 
# 
# 
# Given an array nums representing the data status of this set after the error.
# Your task is to firstly find the number occurs twice and then find the number
# that is missing. Return them in the form of an array.
# 
# 
# 
# Example 1:
# 
# Input: nums = [1,2,2,4]
# Output: [2,3]
# 
# 
# 
# Note:
# 
# The given array size will in the range [2, 10000].
# The given array's numbers won't have any order.
# 
# 
#
class Solution:
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s = [n for n in range(1,len(nums)+1)]
        j = sum(s) - sum(set(nums))
        if sum(s) > sum(nums):
            i = j - sum(s) + sum(nums)
        else:
            i = j - sum(s) + sum(nums)
            

        return [i,j]
        
if __name__ == "__main__":
    print(Solution().findErrorNums([2,2]))