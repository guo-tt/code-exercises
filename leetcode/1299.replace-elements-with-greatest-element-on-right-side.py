#
# @lc app=leetcode id=1299 lang=python3
#
# [1299] Replace Elements with Greatest Element on Right Side
#

# @lc code=start
class Solution:
    def replaceElements(self, arr):
        a = []
        for i in range(len(arr)): 
            if i + 1 < len(arr):   
                a.append(max(arr[i+1:]))
            if i + 1 == len(arr): 
                a.append(-1)
        return a 
        
# @lc code=end
if __name__ == "__main__":
    print(Solution().replaceElements([17,18,5,4,6,1]))
