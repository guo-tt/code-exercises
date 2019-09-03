#
# @lc app=leetcode id=819 lang=python3
#
# [819] Most Common Word
#
from collections import Counter  
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        for char in '-.,!?;\'\n':
            paragraph = paragraph.replace(char, ' ')
        paragraph = paragraph.lower()

        word_list = paragraph.split()
        i = 1
        j = 0
        while i < len(Counter(word_list)) + 1:
            word, num = Counter(word_list).most_common(i)[j]
            if word not in banned:
                return word
            else:
                i = i + 1
                j = j + 1
        

