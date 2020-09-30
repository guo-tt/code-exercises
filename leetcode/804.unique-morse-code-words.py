#
# @lc app=leetcode id=804 lang=python3
#
# [804] Unique Morse Code Words
#

# @lc code=start
class Solution:
    def uniqueMorseRepresentations(self, words) -> int:
        check = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        morse_word = []
        for word in words:
            s = ""
            for i in range(len(word)):
                s = s + check[ord(word[i])-97]
            morse_word.append(s)
        
        return len(set(morse_word))
# @lc code=end

if __name__ == "__main__":
    print(Solution().uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))