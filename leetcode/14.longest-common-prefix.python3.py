#
# [14] Longest Common Prefix
#
# https://leetcode.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (31.73%)
# Total Accepted:    290.6K
# Total Submissions: 916K
# Testcase Example:  '["flower","flow","flight"]'
#
# Write a function to find the longest common prefix string amongst an array of
# strings.
# 
# If there is no common prefix, return an empty string "".
# 
# Example 1:
# 
# 
# Input: ["flower","flow","flight"]
# Output: "fl"
# 
# 
# Example 2:
# 
# 
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# 
# 
# Note:
# 
# All given inputs are in lowercase letters a-z.
# 
#
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[strf
        :rtype: str
        """
        i = 0
        flag = 1
        t = 0

        if len(strs) == 0: 
           return "" 

        for s in strs:
            if len(s) == 0:
                return ""
            
        if len(strs) == 1:
            return strs[0]

        while i < len(strs[0]) + 1 and flag: 
            for s in strs[1:]:
                if strs[0][:i+1] != s[:i+1]:
                    flag *= 0 
            i += 1
 
        if i >= 1: 
            return strs[0][:i-1]
        elif i == 0:
            return strs[0][0]
        else:
            return ""

if __name__ == '__main__':
    print(Solution().longestCommonPrefix(["cc",""]))
