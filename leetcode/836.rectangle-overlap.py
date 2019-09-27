#
# @lc app=leetcode id=836 lang=python3
#
# [836] Rectangle Overlap
#
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        rec1_x1, rec1_y1, rec1_x2, rec1_y2 = rec1
        rec2_x1, rec2_y1, rec2_x2, rec2_y2 = rec2
        return not (rec1_x1 >= rec2_x2 or rec1_x2 <= rec2_x1 or rec1_y1 >= rec2_y2 or rec1_y2 <= rec2_y1)

