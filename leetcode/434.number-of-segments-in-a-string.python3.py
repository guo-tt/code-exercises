#
# [434] Number of Segments in a String
#
# https://leetcode.com/problems/number-of-segments-in-a-string/description/
#
# algorithms
# Easy (36.56%)
# Total Accepted:    41.8K
# Total Submissions: 114.3K
# Testcase Example:  '"Hello, my name is John"'
#
# Count the number of segments in a string, where a segment is defined to be a
# contiguous sequence of non-space characters.
# 
# Please note that the string does not contain any non-printable characters.
# 
# Example:
# 
# Input: "Hello, my name is John"
# Output: 5
# 
# 
#
class Solution:
    def countSegments(self, s):
        """
        :type s: str
        :rtype: in
        """
        return len(s.split())


if __name__ == '__main__':
    print(Solution().countSegments("             "))
