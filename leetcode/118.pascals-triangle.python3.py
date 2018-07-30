#
# [118] Pascal's Triangle
#
# https://leetcode.com/problems/pascals-triangle/description/
#
# algorithms
# Easy (41.34%)
# Total Accepted:    184.7K
# Total Submissions: 446.8K
# Testcase Example:  '5'
#
# Given a non-negative integer numRows, generate the first numRows of Pascal's
# triangle.
# 
# 
# In Pascal's triangle, each number is the sum of the two numbers directly
# above it.
# 
# Example:
# 
# 
# Input: 5
# Output:
# [
# ⁠    [1],
# ⁠   [1,1],
# ⁠  [1,2,1],
# ⁠ [1,3,3,1],
# ⁠[1,4,6,4,1]
# ]
# 
# 
#
class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
    #     output=[]
    #     for i in range(1,numRows+1):
    #         output.append(self.single(i))
    #     return output

    # def single(self,numRows):
    #     s = [1]

    #     if numRows == 1:
    #         s = [1]
    #         return s
    #     elif numRows == 2:
    #         s = [1,1]
    #         return s
    #     else:
    #         for i in range(1,numRows-1):
    #             s.append(self.single(numRows-1)[i-1]+self.single(numRows-1)[i])
    #         s.append(1)
    #         return s
        if numRows == 0:
            return []
        ret = []
        for i in range(numRows):
            ret.append([1])
            for j in range(1, i + 1):
                if j == i:
                    ret[i].append(1)
                else:
                    ret[i].append(ret[i-1][j-1]+ret[i-1][j])
        return ret


if __name__ == "__main__":
    print(Solution().generate(10))
        
        
