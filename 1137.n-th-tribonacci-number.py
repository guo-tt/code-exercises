#
# @lc app=leetcode id=1137 lang=python3
#
# [1137] N-th Tribonacci Number
#
class Solution:
    def tribonacci(self, n):
        res = [0, 1, 1, 2]
        if n <= 2:
            return res[n]
        cnt = 2
        while cnt < n - 1:
            res[0] = res[1]
            res[1] = res[2]
            res[2] = res[3]
            res[3] = res[0] + res[1] + res[2]
            cnt += 1
            # print res, cnt
        return res[-1]


