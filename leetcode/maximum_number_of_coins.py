# 1561
'''
There are 3n piles of coins of varying size, you and your friends will take piles of coins as follows:

In each step, you will choose any 3 piles of coins (not necessarily consecutive).
Of your choice, Alice will pick the pile with the maximum number of coins.
You will pick the next pile with the maximum number of coins.
Your friend Bob will pick the last pile.
Repeat until there are no more piles of coins.
Given an array of integers piles where piles[i] is the number of coins in the ith pile.

Return the maximum number of coins that you can have.
'''

class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        max_coin = 0
        n = len(piles)
        piles.sort(reverse=True)
        for i in range(n//3):
            max_coin += piles[2*i+1]
        return max_coin
    
# I will make list [Max, min, second maximum]
# So, first list sorting and then take sum piles at i = 1 -> 3 -> ..        

        
if __name__ == '__main__':
    sol = Solution()
    
    for piles in [[2,4,1,2,7,8], [2,4,5], [9,8,7,6,5,1,2,3,4]]:
        print(sol.maxCoins(piles))
        # 9, 4, 18
