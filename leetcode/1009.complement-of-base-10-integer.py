#
# @lc app=leetcode id=1009 lang=python3
#
# [1009] Complement of Base 10 Integer
#

# @lc code=start
class Solution:
    def bitwiseComplement(self, N: int) -> int:
        result = ""
        nbins = bin(N)[2:]
        for i in nbins:
            result += str(int(i)^1)
        return int(result, 2)  


