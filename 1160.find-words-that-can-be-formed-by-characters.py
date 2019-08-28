#
# @lc app=leetcode id=1160 lang=python3
#
# [1160] Find Words That Can Be Formed by Characters
#
class Solution:
    def countCharacters(self, words, chars):
        return len(''.join(filter(lambda x : len(collections.Counter(x) - collections.Counter(chars)) == 0, words)))

