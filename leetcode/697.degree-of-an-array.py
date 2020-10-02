#
# @lc app=leetcode id=697 lang=python3
#
# [697] Degree of an Array
#
from collections import Counter

# @lc code=start
class Solution:
    def findShortestSubArray(self, nums):
        d = dict(Counter(nums))
        key_array=[]
        for k, v in d.items():
            if d[k] == max(d.values()):
                key_array.append(k)

        shortest = 500001
        for i in key_array:
            max_index = 0
            min_index = 500001
            for j in range(len(nums)):  
                if nums[j] == i:
                    if j < min_index:
                        min_index = j
                    if j > max_index: 
                        max_index = j
            if shortest > max_index - min_index:    
                shortest = max_index - min_index
        
        return shortest + 1
                
        # return shortest + 1
# @lc code=end
if __name__ == "__main__":   
    print(Solution().findShortestSubArray([1,2,2,3,1,4,2]))

