#2264. Largest 3-Same-Digit Number in String

'''
You are given a string num representing a large integer. An integer is good if it meets the following conditions:

It is a substring of num with length 3.
It consists of only one unique digit.
Return the maximum good integer as a string or an empty string "" if no such integer exists.

Note:

A substring is a contiguous sequence of characters within a string.
There may be leading zeroes in num or a good integer.
'''

class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """
        for n in range(9,-1,-1):
            num_3_length = '%i'%n * 3
            if num_3_length in num:
                return num_3_length
        return ""

if __name__=='__main__':
    sol = Solution()
    
    for num in ["6777133339", "2300019","42352338"]:
        print(sol.largestGoodInteger(num))