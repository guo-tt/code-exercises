#
# [414] Third Maximum Number
#
# https://leetcode.com/problems/third-maximum-number/description/
#
# algorithms
# Easy (28.20%)
# Total Accepted:    68.6K
# Total Submissions: 243.3K
# Testcase Example:  '[3,2,1]'
#
# Given a non-empty array of integers, return the third maximum number in this
# array. If it does not exist, return the maximum number. The time complexity
# must be in O(n).
# 
# Example 1:
# 
# Input: [3, 2, 1]
# 
# Output: 1
# 
# Explanation: The third maximum is 1.
# 
# 
# 
# Example 2:
# 
# Input: [1, 2]
# 
# Output: 2
# 
# Explanation: The third maximum does not exist, so the maximum (2) is returned
# instead.
# 
# 
# 
# Example 3:
# 
# Input: [2, 2, 3, 1]
# 
# Output: 1
# 
# Explanation: Note that the third maximum here means the third maximum
# distinct number.
# Both numbers with value 2 are both considered as second maximum.
# 
# 
#
import heapq

class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.pool = list(set(nums))
        self.size = len(set(nums))
        heapq.heapify(self.pool)
        while self.size > 3:
            heapq.heappop(self.pool)
            self.size = self.size - 1
        if len(set(nums)) >= 3:
            return self.pool[0]
        else:
            return max(nums)

if __name__ == '__main__':
    print(Solution().thirdMax([1,2]))
        
        
