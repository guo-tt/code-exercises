#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        if not root:
           return False
        if not root.right and not root.left:
            if root.val == sum:
                return True
            else:
                return False
        else:
            return self.hasPathSum(root.right,sum-root.val) or self.hasPathSum(root.left,sum-root.val)

