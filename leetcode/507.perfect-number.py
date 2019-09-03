#
# @lc app=leetcode id=507 lang=python3
#
# [507] Perfect Number
#
class Solution:
    def checkPerfectNumber(self, num):
        import math
        if num <= 1:
            return False
        
        sum_val = 1
        for i in range(2,int(math.sqrt(num))+1):
            if num % i == 0:
                sum_val = sum_val + i + num/i 
            if i == num / i:
                break
        return num == sum_val
        
solution = Solution()
print(solution.checkPerfectNumber(28))
