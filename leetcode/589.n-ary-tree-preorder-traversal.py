#
# @lc app=leetcode id=589 lang=python3
#
# [589] N-ary Tree Preorder Traversal
#
"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def preorder(self, root):
        res = []
        if not root:
            return res
        res.append(root.val)
        for child in root.children:
            res.extend(self.preorder(child))
        return res

