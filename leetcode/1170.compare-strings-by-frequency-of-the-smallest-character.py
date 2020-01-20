#
# @lc app=leetcode id=1170 lang=python3
#
# [1170] Compare Strings by Frequency of the Smallest Character
#
class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        record = []
        for word in words:
            record.append(self.func(word))
        record.sort()
        # print record
        
        n = len(record)
        res = []
        for q in queries:
            fq = self.func(q)
            cnt = 0
            for num in record:
                if num <= fq:
                    cnt += 1
                else:
                    break
            res.append(n - cnt)
        return res
    
    def func(self, word):
        for char in "abcdefghijklmnopqrstuvwxyz":
            t = word.count(char) 
            if t > 0:
                return t
        return 0



