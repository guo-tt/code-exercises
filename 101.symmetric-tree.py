#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True

        return self.isSymmetricNodes(root.left, root.right)

    def isSymmetricNodes(self, l, r):

        if l is None and r is None:
            return True
        elif l is None or r is None:
            return False

        return (l.val == r.val) and  self.isSymmetricNodes(l.left, r.right) and self.isSymmetricNodes(l.right, r.left)

        
