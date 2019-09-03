#
# @lc app=leetcode id=107 lang=python3
#
# [107] Binary Tree Level Order Traversal II
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preOrder(self, root, level, res):
        if root:
            if len(res)<level+1:
                res.append([])
            res[level].append(root.val)
            self.preOrder(root.left, level+1, res)
            self.preOrder(root.right, level+1, res)

    def levelOrderBottom(self, root):
        res = []
        self.preOrder(root, 0, res)
        res.reverse()
        return res 
        

