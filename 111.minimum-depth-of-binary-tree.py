#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def level(self, l, root):
        if root:
            l = l + 1 
            return min(self.level(l, root.right), self.level(l, root.left)) 
        else:
            return l

    def minDepth(self, root):
        l = 0
        return self.level(l, root)
        

