#
# @lc app=leetcode id=832 lang=python3
#
# [832] Flipping an Image
#
class Solution:
    def flipAndInvertImage(self, A):
        return [[1-b for b in a[::-1]] for a in A]
