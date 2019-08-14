#
# @lc app=leetcode id=989 lang=python3
#
# [989] Add to Array-Form of Integer
#
class Solution:
    def addToArrayForm(self, A, K):
        a = 0
        for i in A:
            a = a*10 + i
            
        tmp = a + K
        if tmp == 0:
            return [0]
        res= list()
        while tmp:
            res.insert(0, tmp%10)
            tmp //= 10
        return res

