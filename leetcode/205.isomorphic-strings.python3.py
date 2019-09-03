#
# [205] Isomorphic Strings
#
# https://leetcode.com/problems/isomorphic-strings/description/
#
# algorithms
# Easy (35.18%)
# Total Accepted:    147.4K
# Total Submissions: 419.1K
# Testcase Example:  '"egg"\n"add"'
#
# Given two strings s and t, determine if they are isomorphic.
# 
# Two strings are isomorphic if the characters in s can be replaced to get t.
# 
# All occurrences of a character must be replaced with another character while
# preserving the order of characters. No two characters may map to the same
# character but a character may map to itself.
# 
# Example 1:
# 
# 
# Input: s = "egg", t = "add"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: s = "foo", t = "bar"
# Output: false
# 
# Example 3:
# 
# 
# Input: s = "paper", t = "title"
# Output: true
# 
# Note:
# You may assume both s and t have the same length.
# 
#
class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        st=[]
        for i in range(0,len(s)):
            st.append(ord(s[i]) - ord(t[i]))

        if len(set(s)) != len(set(t)):
            return False

        dict={}
        for i in range(0,len(s)):
            if s[i] not in dict:
                dict[s[i]] = st[i]
            else:
                if dict[s[i]] != st[i]:
                    return False
        return True

if __name__ == "__main__":
    print(Solution().isIsomorphic("ab","aa"))