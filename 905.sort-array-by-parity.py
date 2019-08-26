#
# @lc app=leetcode id=905 lang=python3
#
# [905] Sort Array By Parity
#
class Solution:
    def sortArrayByParity(self, A):
        evenarray = [a for a in A if a%2 == 0]
        oddarray = [a for a in A if a%2 == 1]
        #print(evenarray + oddarray)

        return evenarray + oddarray
        

