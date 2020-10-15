#
# @lc app=leetcode id=961 lang=python3
#
# [961] N-Repeated Element in Size 2N Array
#
from collections import Counter
# @lc code=start
class Solution:
    def repeatedNTimes(self, A):
        for key, value in Counter(A).items():
            if value == len(A)//2:
                return key
# @lc code=end
if __name__ == "__main__":
    print(Solution().repeatedNTimes([5,1,5,2,5,3,5,4]))
