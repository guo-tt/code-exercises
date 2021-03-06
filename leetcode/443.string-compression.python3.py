#
# [443] String Compression
#
# https://leetcode.com/problems/string-compression/description/
#
# algorithms
# Easy (35.64%)
# Total Accepted:    24.5K
# Total Submissions: 68.7K
# Testcase Example:  '["a","a","b","b","c","c","c"]'
#
# Given an array of characters, compress it in-place.
# 
# The length after compression must always be smaller than or equal to the
# original array.
# 
# Every element of the array should be a character (not int) of length 1.
# ⁠
# After you are done modifying the input array in-place, return the new length
# of the array.
# 
# 
# 
# Follow up:
# Could you solve it using only O(1) extra space?
# 
# 
# 
# 
# Example 1:
# 
# Input:
# ["a","a","b","b","c","c","c"]
# 
# Output:
# Return 6, and the first 6 characters of the input array should be:
# ["a","2","b","2","c","3"]
# 
# Explanation:
# "aa" is replaced by "a2". "bb" is replaced by "b2". "ccc" is replaced by
# "c3".
# 
# 
# 
# Example 2:
# 
# Input:
# ["a"]
# 
# Output:
# Return 1, and the first 1 characters of the input array should be: ["a"]
# 
# Explanation:
# Nothing is replaced.
# 
# 
# 
# Example 3:
# 
# Input:
# ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
# 
# Output:
# Return 4, and the first 4 characters of the input array should be:
# ["a","b","1","2"].
# 
# Explanation:
# Since the character "a" does not repeat, it is not compressed. "bbbbbbbbbbbb"
# is replaced by "b12".
# Notice each digit has it's own entry in the array.
# 
# 
# 
# Note:
# 
# All characters have an ASCII value in [35, 126].
# 1 .
# 
# 
#
class Solution:
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        # dict = {}
        # for i in range(0,len(chars)):
        #     if chars[i] not in dict:
        #         dict[chars[i]] = 1
        #     else:
        #         dict[chars[i]] += 1
        # return dict
        anchor = write = 0
        for read, c in enumerate(chars):
            if read + 1 == len(chars) or chars[read + 1] != c:
                chars[write] = chars[anchor]
                write += 1
                if read > anchor:
                    for digit in str(read - anchor + 1):
                        chars[write] = digit
                        write += 1
                anchor = read + 1
        return write

if __name__ == '__main__':
    print(Solution().compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))
        
