#
# [541] Reverse String II
#
# https://leetcode.com/problems/reverse-string-ii/description/
#
# algorithms
# Easy (44.24%)
# Total Accepted:    46.1K
# Total Submissions: 104.2K
# Testcase Example:  '"abcdefg"\n2'
#
# 
# Given a string and an integer k, you need to reverse the first k characters
# for every 2k characters counting from the start of the string. If there are
# less than k characters left, reverse all of them. If there are less than 2k
# but greater than or equal to k characters, then reverse the first k
# characters and left the other as original.
# 
# 
# Example:
# 
# Input: s = "abcdefg", k = 2
# Output: "bacdfeg"
# 
# 
# 
# Restrictions: 
# 
# ⁠The string consists of lower English letters only.
# ⁠Length of the given string and k will in the range [1, 10000]
# 
#
class Solution:
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        output = ""
        if len(s) < k:
            return s[::-1]
        elif len(s) < 2*k:
            return s[k-1::-1] + s[k:]
        else:
            for i in range(0,len(s)):
                if (i+1)%2 == 0:
                    output += s[i:i-k:-1]
            return output
        
if __name__ == "__main__":
    print(Solution().reverseStr("abcdefg",2))

        
