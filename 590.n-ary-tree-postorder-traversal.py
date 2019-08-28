#
# @lc app=leetcode id=590 lang=python3
#
# [590] N-ary Tree Postorder Traversal
#
"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root):
        if not root:
            return []
        if not root.children:
            return [root.val]
        result = []
        for child in root.children:
            result += self.postorder(child)
        result += [root.val]
        return result


        

