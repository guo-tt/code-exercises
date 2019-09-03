#
# @lc app=leetcode id=821 lang=python3
#
# [821] Shortest Distance to a Character
#
class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        index_nums = []
        for i, letter in enumerate(S):
            if letter == C:
                index_nums.append(i)

        ans = []
        for j, word in enumerate(S):
            distance = [abs(j - index_num) for index_num in index_nums]
            ans.append(min(distance))
            
        return ans

        
        

        

