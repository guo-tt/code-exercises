#
# @lc app=leetcode id=682 lang=python3
#
# [682] Baseball Game
#
class Solution:
    #def calPoints(self, ops: List[str]) -> int:
    def calPoints(self, ops):
        output = []
        for i in range(0,len(ops)):
            if ops[i] != "+" and ops[i] != "D" and ops[i] != "C":
                output.append(int(ops[i]))
            if ops[i] == "D":
                l = len(output)
                output.append(2*int(output[l-1]))
            if ops[i] == "C":
                output.pop()
            if ops[i] == "+":
                output.append(sum(output[-2:]))
        return sum([n for n in output])
            

        

