#
# @lc app=leetcode id=717 lang=python3
#
# [717] 1-bit and 2-bit Characters
#
class Solution:
    def isOneBitCharacter(self, bits):
        pos = 0
        while pos < len(bits) - 1:
            if bits[pos] == 1: 
                pos += 2 
            else: 
                pos += 1
            
        return pos == len(bits) - 1 and bits[pos] == 0

        


