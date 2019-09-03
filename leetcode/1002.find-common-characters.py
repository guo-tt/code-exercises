#
# @lc app=leetcode id=1002 lang=python3
#
# [1002] Find Common Characters
#
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        output = []
        for i in range(0,len(A[0])):
            c = A[0][i]
            flag = 1
            for j in range(1,len(A)):
                if c not in A[j]:
                    flag = 0
            if flag:
                output.append(c)
                for j in range(1,len(A)):
                    A[j] = A[j].replace(c,'',1)
        return output
