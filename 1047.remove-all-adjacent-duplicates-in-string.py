#
# @lc app=leetcode id=1047 lang=python3
#
# [1047] Remove All Adjacent Duplicates In String
#
class Solution:
    def removeDuplicates(self, S):

        stack = []
        for s in S:
            if stack and s == stack[-1]:
                stack.pop()
                continue
            stack.append(s)
        return "".join(stack)

