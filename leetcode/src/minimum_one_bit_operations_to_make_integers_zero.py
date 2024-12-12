# 1611. Minimum One Bit Operations to Make Integers Zero

'''
Given an integer n, you must transform it into 0 using the following operations any number of times:

Change the rightmost (0th) bit in the binary representation of n.
Change the ith bit in the binary representation of n if the (i-1)th bit is set to 1 and the (i-2)th through 0th bits are set to 0.
Return the minimum number of operations to transform n into 0.
'''

class Solution(object):
    def minimumOneBitOperations(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        n = n^self.minimumOneBitOperations(n>>1)
        return n
        
        

if __name__ == '__main__':
    sol = Solution()
    for n in [3,6]:
        print(sol.minimumOneBitOperations(n))