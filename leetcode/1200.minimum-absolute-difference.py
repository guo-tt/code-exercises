#
# @lc app=leetcode id=1200 lang=python3
#
# [1200] Minimum Absolute Difference
#

# @lc code=start
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        mindiff=2000001 # set the max diff first
        rst=[]
        for i in range(1,len(arr)): # find the mindiff
            if arr[i]-arr[i-1] < mindiff:
                mindiff = arr[i]-arr[i-1]
        for i in range(1,len(arr)):    #find the diff equal to mindiff
            if arr[i]-arr[i-1] == mindiff:
                rst.append([arr[i-1],arr[i]])
        return rst

        
# @lc code=end

