#
# @lc app=leetcode id=1108 lang=python3
#
# [1108] Defanging an IP Address
#
class Solution:
    def defangIPaddr(self, address):
        return address.replace('.','[.]')
        

