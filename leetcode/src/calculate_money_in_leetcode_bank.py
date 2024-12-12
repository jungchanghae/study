# 1716. Calculate Money in Leetcode Bank

'''
Hercy wants to save money for his first car. He puts money in the Leetcode bank every day.

He starts by putting in $1 on Monday, the first day. Every day from Tuesday to Sunday, he will put in $1 more than the day before. On every subsequent Monday, he will put in $1 more than the previous Monday.
Given n, return the total amount of money he will have in the Leetcode bank at the end of the nth day.
'''

class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        for i in range(1,n//7 + 1):
            result += self.sum_of_week(i)
        
        result += self.sum_of_week(n//7 + 1,n%7)
        return result
    
    def sum_of_week(self, start_money, end_n=7):
        return (start_money-1)*end_n + end_n*(end_n+1)//2
        
if __name__=='__main__':
    sol = Solution()
    for n in [4, 10, 20]:
        print(sol.totalMoney(n))
        