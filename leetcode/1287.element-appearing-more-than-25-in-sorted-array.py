#
# @lc app=leetcode id=1287 lang=python3
#
# [1287] Element Appearing More Than 25% In Sorted Array
#

# @lc code=start
class Solution:
    def findSpecialInteger(self, arr):

        appearence = int(len(arr)/4)
        print(appearence)

        count_a = 0

        if len(arr) == 1:
            return arr[0]
        else:  
            for i in range(len(arr)):
                if i + 1 <= len(arr) - 1:
                    if arr[i+1] == arr[i]: 
                        count_a = count_a + 1
                    else: 
                        count_a = 0
                    if count_a + 1 > appearence:  
                        return arr[i+1]
# @lc code=end
if __name__ == "__main__":
    print(Solution().findSpecialInteger([1,1,2,2,3,3,3,3]))
