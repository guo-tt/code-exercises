#
# [551] Student Attendance Record I
#
# https://leetcode.com/problems/student-attendance-record-i/description/
#
# algorithms
# Easy (44.94%)
# Total Accepted:    40.1K
# Total Submissions: 89.1K
# Testcase Example:  '"PPALLP"'
#
# You are given a string representing an attendance record for a student. The
# record only contains the following three characters:
# 
# 
# 
# 'A' : Absent. 
# 'L' : Late.
# ⁠'P' : Present. 
# 
# 
# 
# 
# A student could be rewarded if his attendance record doesn't contain more
# than one 'A' (absent) or more than two continuous 'L' (late).    
# 
# You need to return whether the student could be rewarded according to his
# attendance record.
# 
# Example 1:
# 
# Input: "PPALLP"
# Output: True
# 
# 
# 
# Example 2:
# 
# Input: "PPALLL"
# Output: False
# 
# 
# 
# 
# 
#
class Solution:
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        suma = 0
        for i in range(0,len(s)):
            if s[i] == "A":
                suma += 1
                if suma > 1:
                    return False
            if s[i] == "L" and i > 1:
                if s[i-1] == "L" and s[i-2] == "L":
                    return False
        return True

if __name__ == "__main__":
    print(Solution().checkRecord("PLALL"))
