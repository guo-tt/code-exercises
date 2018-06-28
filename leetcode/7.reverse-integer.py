#!C:\Python27\Python

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        nlen = len(str(x))
        output = ""
        while nlen > 0:
            output += str(x)[nlen-1]
            nlen = nlen - 1

        if output[-1] == '-':
            output = output[:-1]
            if int(output) > 0x7fffffff:
                return 0
            else:
                return 0 - int(output)
        else:
            if int(output) > 0x7fffffff:
                return 0
            else:
                return int(output)
            
if __name__ == '__main__':
    print(Solution().reverse(123))        
