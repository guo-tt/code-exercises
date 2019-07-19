#
# @lc app=leetcode id=566 lang=python3
#
# [566] Reshape the Matrix
#
class Solution:
    def matrixReshape(self, nums: List[List[int]], r, c):
        M = len(nums)
        N = len(nums[0])

        res = []
        row = []
        if M*N != r*c:
            return nums
        for i in range(0,M):
            for j in range(0,N):
                row.append(nums[i][j])
                if len(row) == c:
                    res.append(row)
                    row = []
        return res
        


        

