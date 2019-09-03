#
# [463] Island Perimeter
#
# https://leetcode.com/problems/island-perimeter/description/
#
# algorithms
# Easy (58.83%)
# Total Accepted:    102.9K
# Total Submissions: 174.8K
# Testcase Example:  '[[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]'
#
# You are given a map in form of a two-dimensional integer grid where 1
# represents land and 0 represents water.
# 
# Grid cells are connected horizontally/vertically (not diagonally). The grid
# is completely surrounded by water, and there is exactly one island (i.e., one
# or more connected land cells).
# 
# The island doesn't have "lakes" (water inside that isn't connected to the
# water around the island). One cell is a square with side length 1. The grid
# is rectangular, width and height don't exceed 100. Determine the perimeter of
# the island.
# 
# 
# 
# Example:
# 
# 
# Input:
# [[0,1,0,0],
# ⁠[1,1,1,0],
# ⁠[0,1,0,0],
# ⁠[1,1,0,0]]
# 
# Output: 16
# 
# Explanation: The perimeter is the 16 yellow stripes in the image below:
# 
# 
# 
# 
#
class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        c = len(grid)
        if c:
            r = len(grid[0])

        count = 0

        for i in range(0,c):
           for j in range(0,r):
               if grid[i][j] == 1:
                    # if i and j and grid[i-1][j] and grid[i][j-1]: 
                    #    pass 
                    # elif (not i or grid[i-1][j] == 0) and (not j or grid[i][j-1] == 0): 
                    #     count += 4
                    # else: count += 2
                    count = count + 4
                    if i>0 and grid[i-1][j]==1:
                        count = count -2
                    if j>0 and grid[i][j-1]==1:
                        count = count -2
                    # if i != 0:
                    #     if grid[i-1][j] == 0:
                    #         count += 1
                    # if i != c-1:
                    #     if grid[i+1][j] == 0:
                    #         count += 1
                    # if j != 0:
                    #     if grid[i][j-1] == 0:
                    #         count += 1
                    # if j != r-1:
                    #     if grid[i][j+1] == 0:
                    #         count += 1

        return count

if __name__ == "__main__":
    print(Solution().islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))
                    
                    


        
