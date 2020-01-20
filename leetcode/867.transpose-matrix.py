#
# @lc app=leetcode id=867 lang=python3
#
# [867] Transpose Matrix
#
class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        rows, cols = len(A), len(A[0])
        res = [[0] * rows for _ in range(cols)]
        for row in range(rows):
            for col in range(cols):
                res[col][row] = A[row][col]
        return res


