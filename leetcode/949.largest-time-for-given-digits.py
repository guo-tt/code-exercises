#
# @lc app=leetcode id=949 lang=python3
#
# [949] Largest Time for Given Digits
#
class Solution:
    def largestTimeFromDigits(self, A):
        A.sort()
        for h in range(23, -1, -1):
            for m in range(59, -1, -1):
                t = [int(h / 10), h % 10, int(m / 10), m % 10]
                ts = sorted(t)
                if ts == A:
                    return str(t[0]) + str(t[1]) + ":" + str(t[2]) + str(t[3])
        return ""
