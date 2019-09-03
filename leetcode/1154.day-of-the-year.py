#
# @lc app=leetcode id=1154 lang=python3
#
# [1154] Day of the Year
#
class Solution:
    def dayOfYear(self, date):
        d1 = [31,28,31,30,31,30,31,31,30,31,30,31]
        d2 = [31,29,31,30,31,30,31,31,30,31,30,31]

        year = int(date.split('-')[0])
        month = int(date.split('-')[1])
        day = int(date.split('-')[2])

        flag = 0 
        if year%400 == 0:
            flag = 1 
        if year%4 == 0 and year%100 != 0:
            flag = 1 

        s = 0 
        m = month - 2
        if flag == 0:
            while m >= 0:
                s += d1[m]
                m = m - 1 
            s = s + day  
        if flag == 1:
            while m >= 0:
                s += d2[m] 
                m = m - 1
            s = s + day 

        return s  


