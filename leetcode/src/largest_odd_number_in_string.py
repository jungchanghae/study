# 1903. Largest Odd Number in String

'''
You are given a string num, representing a large integer. 
Return the largest-valued odd integer (as a string) that is a non-empty substring of num, or an empty string "" if no odd integer exists.
A substring is a contiguous sequence of characters within a string.
'''

class Solution(object):
    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """
        length = len(num)-1
        for l in range(length,-1,-1):
            n = num[l]
            if  int(n) % 2 == 1:
                return num[:l+1]
        return ''
# 최대 길이 substring부터 살펴보기
# 길이가 가장 길 때 홀수가 가장 크다.
# 뒤에서부터 홀수가 등장했을 때 처음부터 거기까지의 길이가 가장 길다.

if __name__=='__main__':
    sol = Solution()
    for n in ['52', '4206', '35427']:
        print(sol.largestOddNumber(n))