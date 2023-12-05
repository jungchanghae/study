# 1688. Count of Matches in Tournament

'''
You are given an integer n, the number of teams in a tournament that has strange rules:

If the current number of teams is even, each team gets paired with another team. A total of n / 2 matches are played, and n / 2 teams advance to the next round.
If the current number of teams is odd, one team randomly advances in the tournament, and the rest gets paired. A total of (n - 1) / 2 matches are played, and (n - 1) / 2 + 1 teams advance to the next round.
Return the number of matches played in the tournament until a winner is decided.
'''

class Solution(object):
    def numberOfMatches(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Recursive
        # if n == 1:
        #     return 0
        
        # if n == 2:
        #     return 1
        # else:
        #     return n//2 + self.numberOfMatches((n-1)//2 + 1 if n%2 else n//2)
        
        result = 0
        while n > 1:
            if n % 2:
                result += (n-1)//2
                n = (n-1)//2 + 1
            else:
                result += n//2
                n = n//2
        return result
        
if __name__ == '__main__':
    sol = Solution()
    for n in [7, 14]:
        print(sol.numberOfMatches(n))