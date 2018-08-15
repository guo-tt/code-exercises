#
# [438] Find All Anagrams in a String
#
# https://leetcode.com/problems/find-all-anagrams-in-a-string/description/
#
# algorithms
# Easy (34.13%)
# Total Accepted:    73.5K
# Total Submissions: 215.4K
# Testcase Example:  '"cbaebabacd"\n"abc"'
#
# Given a string s and a non-empty string p, find all the start indices of p's
# anagrams in s.
# 
# Strings consists of lowercase English letters only and the length of both
# strings s and p will not be larger than 20,100.
# 
# The order of output does not matter.
# 
# Example 1:
# 
# Input:
# s: "cbaebabacd" p: "abc"
# 
# Output:
# [0, 6]
# 
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
# 
# 
# 
# Example 2:
# 
# Input:
# s: "abab" p: "ab"
# 
# Output:
# [0, 1, 2]
# 
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".
# 
# 
#
import collections

class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        # output = []
        # lp = len(p)
        # sp = ''.join(sorted(p))

        # for i in range(0,len(s)):
        #     si = ''.join(sorted(s[i:i+lp]))
        #     if si == sp:
        #         output.append(i)

        # return output
        d = collections.defaultdict(int)
        ns = len(s)
        np = len(p)
        ans = []
        
        for c in p:	
            d[c] -= 1
        
        for i in range(0,ns):
            if i < np:
                d[s[i]] += 1
                if not d[s[i]]: 
                    del d[s[i]]
            else:
                if not d: 
                    ans.append(i-np)

                d[s[i-np]] -= 1

                if not d[s[i-np]] : 
                    del d[s[i-np]]
                
                d[s[i]] += 1
                
                if not d[s[i]]: 
                    del d[s[i]]
        
        if not d: 
            ans.append(i-np+1)
            
        return ans
    
if __name__ == "__main__":
    print(Solution().findAnagrams("cbaebabacd","abc"))
        
