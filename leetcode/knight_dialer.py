# 935. Knight Dialer

'''
The chess knight has a unique movement, it may move two squares vertically and one square horizontally, or two squares horizontally and one square vertically (with both forming the shape of an L). 
Given an integer n, return how many distinct phone numbers of length n we can dial.

You are allowed to place the knight on any numeric cell initially and then you should perform n - 1 jumps to dial a number of length n. All jumps should be valid knight jumps.

As the answer may be very large, return the answer modulo 10^9 + 7.
'''

class Solution(object):
    def knightDialer(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 0 -> 4, 6
        # 1 -> 6, 8
        # 2 -> 7, 9
        # 3 -> 4, 8
        # 4 -> 0, 3, 9
        # 5 -> x
        # 6 -> 0, 1, 7
        # 7 -> 2, 6
        # 8 -> 1, 3
        # 9 -> 2, 4
        # 이동가능한 경우의 수
        result = [1] * 10
        
        if n == 1:
            return sum(result) % (10**9 + 7)
            
        for i in range(n-1):
            result = [result[4] + result[6], result[6] + result[8], result[7] + result[9],
                      result[4] + result[8], result[0] + result[3] + result[9], 0, result[0] + result[1] + result[7],
                      result[2] + result[6], result[1] + result[3], result[2] + result[4]]
        return sum(result) % (10**9 + 7)


if __name__ == '__main__':
    sol = Solution()
    for n in [1,2,3131]:
        print(sol.knightDialer(n))
        
    # 10, 20, 136006598