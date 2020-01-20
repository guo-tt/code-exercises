#
# @lc app=leetcode id=1037 lang=python3
#
# [1037] Valid Boomerang
#
class Solution:
    def isBoomerang(self, points):
        x1, x2, x3 = points[0][0], points[1][0], points[2][0]
        y1, y2, y3 = points[0][1], points[1][1], points[2][1]
        
        return (x1*y2-x2*y1)+(x2*y3-x3*y2)+(x3*y1-x1*y3) != 0

        
