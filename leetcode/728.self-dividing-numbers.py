#
# @lc app=leetcode id=728 lang=python3
#
# [728] Self Dividing Numbers
#
class Solution:
    def isSelfDivide(self,num):
        if '0' in str(num):
            return False
        return 0 == sum(num % int(i) for i in str(num))

    def selfDividingNumbers(self, left, right):
        output = []
        for i in range(left, right+1):
            if self.isSelfDivide(i):
                output.append(i)
        return output
        
