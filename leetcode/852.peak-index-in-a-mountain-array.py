#
# @lc app=leetcode id=852 lang=python3
#
# [852] Peak Index in a Mountain Array
#

# @lc code=start
class Solution:
    def peakIndexInMountainArray(self, arr):
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                return i
# @lc code=end

if __name__ == "__main__":
    print(Solution().peakIndexInMountainArray([3,4,5,1]))

