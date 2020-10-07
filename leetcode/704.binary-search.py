#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#

# @lc code=start
class Solution:
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1
        while right >= left: 
            mid = (right + left)//2 
            if target == nums[mid]:
                return mid
            elif nums[mid] > target:
                right = mid - 1#
            else: 
                left = mid + 1#
        else: 
            return -1

# @lc code=end
if __name__ == "__main__":
    print(Solution().search([-1,0,3,5,9,12], 9))
