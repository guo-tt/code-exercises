#
# @lc app=leetcode id=1089 lang=python3
#
# [1089] Duplicate Zeros
#
class Solution:
    def duplicateZeros(self, arr):
        """
        Do not return anything, modify arr in-place instead.
        """
        i, n = 0, len(arr)
        stack = []
        while i < n:
            stack.append(arr[i])
            t = stack.pop(0)             
            if t == 0:
                arr[i] = 0
                if i+1<n:
                    stack.append(arr[i+1])
                    arr[i+1] = 0
                i+=1
            else:
                arr[i] = t
            i += 1 

