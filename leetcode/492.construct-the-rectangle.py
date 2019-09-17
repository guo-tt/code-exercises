#
# @lc app=leetcode id=492 lang=python3
#
# [492] Construct the Rectangle
#
import math  

class Solution:
    def constructRectangle(self, area):
        sqr = int(math.sqrt(area))
        while (area % sqr != 0):
            sqr -= 1
        return [int(area / sqr), sqr]
        
