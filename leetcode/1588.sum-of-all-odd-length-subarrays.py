#
# @lc app=leetcode id=1588 lang=python3
#
# [1588] Sum of All Odd Length Subarrays
#

# @lc code=start
class Solution:
    def sumOddLengthSubarrays(self, arr):
        len_count = []
        for i in range(len(arr)):
            if i%2 == 0:   
                len_count.append(i)

        # result = []
        output = 0
        for c in len_count:
            for i in range(len(arr)):
                if i + c + 1 <= len(arr):
                    temp = arr[i: i + c + 1]
                    output = output + sum(temp)
                    # result.append(temp)

        return output
        
# @lc code=end
if __name__ == "__main__":
    print(Solution().sumOddLengthSubarrays([10,11,12]))
