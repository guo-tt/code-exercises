#
# @lc app=leetcode id=637 lang=python3
#
# [637] Average of Levels in Binary Tree
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root):
        ans = []
        que = [root]

        while que:
            ans.append(1.0*sum([n.val for n in que])/len(que))
            nque = []
            for n in que:
                if n.left: 
                    nque.append(n.left)
                if n.right:
                    nque.append(n.right)
            que = nque
        return ans

