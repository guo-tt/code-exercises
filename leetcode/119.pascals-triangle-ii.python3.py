#
# [119] Pascal's Triangle II
#
# https://leetcode.com/problems/pascals-triangle-ii/description/
#
# algorithms
# Easy (39.29%)
# Total Accepted:    155.6K
# Total Submissions: 396K
# Testcase Example:  '3'
#
# Given a non-negative index k where k ≤ 33, return the kth index row of the
# Pascal's triangle.
# 
# Note that the row index starts from 0.
# 
# 
# In Pascal's triangle, each number is the sum of the two numbers directly
# above it.
# 
# Example:
# 
# 
# Input: 3
# Output: [1,3,3,1]
# 
# 
# Follow up:
# 
# Could you optimize your algorithm to use only O(k) extra space?
# 
#
class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        ret = []
        for i in range(rowIndex+1):
            ret.append([1])
            for j in range(1, i + 1):
                if j == i:
                    ret[i].append(1)
                else:
                    ret[i].append(ret[i-1][j-1]+ret[i-1][j])
        return ret[rowIndex]


if __name__ == "__main__":
    print(Solution().getRow(3))
