#
# [88] Merge Sorted Array
#
# https://leetcode.com/problems/merge-sorted-array/description/
#
# algorithms
# Easy (32.69%)
# Total Accepted:    250.1K
# Total Submissions: 765.2K
# Testcase Example:  '[1,2,3,0,0,0]\n3\n[2,5,6]\n3'
#
# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as
# one sorted array.
# 
# Note:
# 
# 
# The number of elements initialized in nums1 and nums2 are m and n
# respectively.
# You may assume that nums1 has enough space (size that is greater or equal to
# m + n) to hold additional elements from nums2.
# 
# 
# Example:
# 
# 
# Input:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
# 
# Output: [1,2,2,3,5,6]
# 
# 
#
class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        p = m - 1
        q = n - 1
        while p >= 0 and q >= 0:
            if nums1[p] < nums2[q]:
                nums1[p+q+1] = nums2[q]
                q -= 1
            else:
                nums1[p+q+1] = nums1[p]
                p -= 1

        nums1[:q+1] = nums2[:q+1]

if __name__ == '__main__':
    #print(Solution().merge([1,0],1,[2],1))
    print(Solution().merge([4,0,0,0,0,0],1,[1,2,3,5,6],5))
    #print(Solution().merge([2,0],1,[1],1))
        
