#
# @lc app=leetcode id=1370 lang=python3
#
# [1370] Increasing Decreasing String
#
from collections import Counter
from collections import OrderedDict

# @lc code=start
class Solution:
    def sort_from_begin(self, d): 
        s = ''
        for k, v in d.items():
            if v != 0:
                s = s + k
                d[k] = d[k] - 1 
        return s, d

    def sortString(self, s: str) -> str:
        output = ''
        d = {}
        cnt = Counter(s)
        for key, value in cnt.items():
            d[key] = value

        d = OrderedDict(sorted(d.items()))

        sum_value = 0
        for key, value in d.items():
            sum_value += value

        i = 0
        while sum_value != 0:
            temp, d = self.sort_from_begin(d)
            if i%2 == 0: 
                output = output + temp
            else:   
                output = output + temp[::-1]

            i = i + 1
            sum_value = 0
            for key, value in d.items():
                sum_value += value
                  
        return output

if __name__ == '__main__':
    print(Solution().sortString("spo"))
# @lc code=end

