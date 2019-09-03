#
# @lc app=leetcode id=665 lang=python3
#
# [665] Non-decreasing Array
#
class Solution:
    def checkPossibility(self, nums):
        a,b=nums[:],nums[:]
        if len(nums)>2:
            for i in range(1,len(nums)-1):
                if a[i]>a[i+1]:
                    del a[i]
                    del b[i+1]
                    return ((a == sorted(a)) or (b==sorted(b)))

            else:
                return True
        else:
            return True
        

        # return sum(f < 0 for f in a) == 1
        
