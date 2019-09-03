#
# [485] Max Consecutive Ones
#
# https://leetcode.com/problems/max-consecutive-ones/description/
#
# algorithms
# Easy (53.73%)
# Total Accepted:    99.6K
# Total Submissions: 185.3K
# Testcase Example:  '[1,0,1,1,0,1]'
#
# Given a binary array, find the maximum number of consecutive 1s in this
# array.
# 
# Example 1:
# 
# Input: [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive
# 1s.
# ⁠   The maximum number of consecutive 1s is 3.
# 
# 
# 
# Note:
# 
# The input array will only contain 0 and 1.
# The length of input array is a positive integer and will not exceed 10,000
# 
# 
#
class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        f = set()
        flag = 0
        for i in range(0,len(nums)):
            if nums[i] == 1:
                flag += 1
                if i == len(nums)-1:
                    f.add(flag)
            elif nums[i] == 0 and flag > 0:
                f.add(flag)
                flag = 0
        
        if len(f) > 0:
            return max(f)
        else:
            return 0

if __name__ == "__main__":
    print(Solution().findMaxConsecutiveOnes([1,0,1,1,0,1]))