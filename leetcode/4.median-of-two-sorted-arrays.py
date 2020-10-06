#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        num = nums1 + nums2
        num.sort()
        print(num)
        if len(num)%2 == 0:
            l = int((len(num)) / 2) - 1
            r = int((len(num) / 2))
            return (num[l] + num[r]) / 2 
        else:
            if len(num) == 1: 
                return num[0]
            else:
                return num[int(len(num) / 2)]

# @lc code=end
if __name__ == "__main__":
    print(Solution().findMedianSortedArrays([1,2], [3,4]))
