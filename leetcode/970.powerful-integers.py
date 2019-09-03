#
# @lc app=leetcode id=970 lang=python3
#
# [970] Powerful Integers
#
class Solution:
    def powerfulIntegers(self, x, y, bound):
        output = []
        if bound < 2:
            return []
        else:
            for i in range(0,100):
                for j in range(0,100):
                    s = x**i + y**j
                    if s > bound:
                        break
                    if s <= bound:
                        output.append(s)

            for j in range(0,100):
                for j in range(0,100):
                    s = x**i + y**j
                    if s > bound:
                        return sorted(set(output))
                    if s <= bound:
                        output.append(s)
            return sorted(set(output))
