# level: eazy

class Solution(object):
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        max_num = 100
        ans = 0
        # define a matrix to judge prime
        # prime is 0
        prime_matrix = [0] * max_num
        # prime_matrix[2] = prime_matrix[3] = 1
        prime_matrix[1] = -1
        for i in range(2, max_num):
            if prime_matrix[i] == 0:
                num = i ** 2
                while num < max_num:
                    prime_matrix[num] = 1
                    num += i
        # print prime_matrix

        for num in range(L, R + 1):
            b_num = bin(num)[2:]
            if prime_matrix[b_num.count('1')] == 0:
                ans += 1
        return ans