#
# @lc app=leetcode id=599 lang=python3
#
# [599] Minimum Index Sum of Two Lists
#
class Solution:
    def findRestaurant(self, list1, list2):
        dic1 = {word:ind for ind,word in enumerate(list1)}
        dic2 = {word:ind for ind,word in enumerate(list2)}
        answer = []
        smallest = 1000000
        for word in dic1:
            if word in dic2:
                _sum = dic1[word] + dic2[word]
                if smallest > _sum:
                    smallest = _sum
                    answer = [word]
                elif smallest == _sum:
                    answer.append(word)
        return answer

