#
# @lc app=leetcode id=884 lang=python3
#
# [884] Uncommon Words from Two Sentences
#
class Solution:
    def uncommonFromSentences(self, A, B):
        count_A = collections.Counter(A.split(' '))
        count_B = collections.Counter(B.split(' '))
        words = list((count_A.keys() | count_B.keys()) - (count_A.keys() & count_B.keys()))
        ans = []
        for word in words:
            if count_A[word] == 1:
                ans.append(word)
            if count_B[word] == 1:
                ans.append(word)
        return ans
        

