#
# @lc app=leetcode id=1185 lang=python3
#
# [1185] Day of the Week
#
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        import datetime
        whatday = datetime.datetime(year, month, day).strftime("%w")
        return week[int(whatday)]

