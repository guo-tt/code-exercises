#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def height(self, root):
        if root == None:
            return 0
        return max(self.height(root.left),self.height(root.right)) + 1 

    def isBalanced(self, root: TreeNode):
        if root == None:
            return True
        if abs(self.height(root.right)-self.height(root.left)) <= 1:
            return self.isBalanced(root.right) and self.isBalanced(root.left)
        else:
            return False



