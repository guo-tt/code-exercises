#
# @lc app=leetcode id=868 lang=python3
#
# [868] Binary Gap
#

# @lc code=start
class Solution:
    def binaryGap(self, n):
        bi = ""
        while n//2 > 0:
            temp = n%2
            n = n // 2 
            bi = str(temp) + bi
        bi = str(n) + bi 
        
        start = -1
        end = len(bi)
        output = 0
        # print(bi)

        for i in range(len(bi)):
            if bi[i] == "1": 
                if start == -1: 
                    start = i
                    # print("start: " + str(start))
                else: 
                    end = i
                    # print("end: " + str(end))
                    if end - start > output:
                        output = end - start 
                    start = end
                    # print("start: " + str(start))
                    # print("output:" + str(output))
        return output
        
# @lc code=end
if __name__ == "__main__":
    print(Solution().binaryGap(5))
