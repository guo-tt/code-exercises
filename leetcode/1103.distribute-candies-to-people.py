#
# @lc app=leetcode id=1103 lang=python3
#
# [1103] Distribute Candies to People
#
class Solution:
    def distributeCandies(self, candies, num_people):
        res = [0] * num_people
        count = 1
        while candies > 0:
            inx = (count - 1) % num_people
            val = count if candies - count >= 0 else candies
            res[inx] += val
            candies -= val
            count += 1
        return res
        
