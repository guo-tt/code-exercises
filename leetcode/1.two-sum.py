#!C:\Python27\Python

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            if (target - nums[i] in nums) and (i != nums.index(target - nums[i])):
                return [i, nums.index(target - nums[i])]

if __name__ == '__main__':
    print Solution().twoSum([2,3,7],9)

        
        
