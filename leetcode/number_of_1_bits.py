# 191. Number of 1 Bits

'''
Write a function that takes the binary representation of an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

Note:
Note that in some languages, such as Java, there is no unsigned integer type. In this case, the input will be given as a signed integer type.
It should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.

In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 3, the input represents the signed integer. -3.
'''

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return str(bin(n)).count('1')
        # python don't have unsignd integer so use bin()


if __name__== '__main__':
    sol = Solution()
    # test Case
    for n in [7,32, 2**32 -2]:
        print(sol.hammingWeight(n))
        # Answer : 3 1 31
        
    # bin -> ["00000000000000000000000000001011", "00000000000000000000000010000000", "11111111111111111111111111111101"]