#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)

import math  

class Solution:
    def mySqrt(self, x):

        left = 0
        right = x

        while(left <= right):
            mid = math.floor((left + right)/2)

            if(mid*mid < x):
                left = mid + 1

            elif(mid*mid > x):
                right = mid - 1

            else:
                return mid 

        return left - 1 
