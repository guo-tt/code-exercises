#
# @lc app=leetcode id=1122 lang=python3
#
# [1122] Relative Sort Array
#
class Solution:
    def relativeSortArray(self, arr1, arr2):
        not_in_arr2 = []
        dic = {}
        for i in arr1:
            if i in arr2:
                dic[i] = dic.setdefault(i,0) + 1
            else:
                not_in_arr2.append(i)
        res = []
        for i in arr2:
            res += [i]*dic[i]
        return res+sorted(not_in_arr2)

        

