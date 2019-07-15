#
# [204] Count Primes
#
# https://leetcode.com/problems/count-primes/description/
#
# algorithms
# Easy (26.86%)
# Total Accepted:    169.5K
# Total Submissions: 631.2K
# Testcase Example:  '10'
#
# Count the number of prime numbers less than a non-negative number, n.
# 
# Example:
# 
# 
# Input: 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
# 
# 
#
class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # if n == 1 or n == 2 or n == 0:
        #     return 0
        # if n == 3:
        #     return 1
        # if n > 3:
        #     flag = 1
        #     for i in range(2, n-1):
        #         if (n - 1) % i == 0:
        #             flag = 0
        #     return flag + self.countPrimes(n-1)
        if n < 3:
            return 0

        primes = [True] * n
        primes[0] = primes[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                primes[i * i: n: i] = [False] * len(primes[i * i: n: i])
        return sum(primes)

if __name__ == "__main__":
    print(Solution().countPrimes(10))


