#
# @lc app=leetcode id=1592 lang=python3
#
# [1592] Rearrange Spaces Between Words
#

# @lc code=start
class Solution:
    def reorderSpaces(self, text):
        new_text = ""
        str_array = text.split()
        count = len(str_array)
        space_count = text.count(' ')

        if count != 1:
            space_between_words = space_count // (count - 1)
            space_in_end = space_count - space_between_words*(count-1)

            for i in range(len(str_array)-1):
                new_text = new_text + str_array[i]
                new_text = new_text + " "*space_between_words

            new_text = new_text + str_array[-1]
            new_text = new_text + " "*space_in_end
        elif count == 1 and space_count == 0:
            new_text = str_array[0]
        elif count == 1 and space_count > 0:
            new_text = str_array[0] + " "*space_count

        return new_text
# @lc code=end
if __name__ == "__main__":
    print(Solution().reorderSpaces("perfect"))
