# 1630
'''
A sequence of numbers is called arithmetic if it consists of at least two elements, and the difference between every two consecutive elements is the same. More formally, a sequence s is arithmetic if and only if s[i+1] - s[i] == s[1] - s[0] for all valid i.

For example, these are arithmetic sequences:

1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9
The following sequence is not arithmetic:

1, 1, 2, 5, 7
You are given an array of n integers, nums, and two arrays of m integers each, l and r, representing the m range queries, where the ith query is the range [l[i], r[i]]. All the arrays are 0-indexed.

Return a list of boolean elements answer, where answer[i] is true if the subarray nums[l[i]], nums[l[i]+1], ... , nums[r[i]] can be rearranged to form an arithmetic sequence, and false otherwise.

'''

class Solution(object):
    def checkArithmeticSubarrays(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: List[int]
        :type r: List[int]
        :rtype: List[bool]
        """
        result = []
        m = len(l)
        n = len(nums)
        for i in range(m):
            sub_arr = [nums[j] for j in range(l[i],r[i]+1)]
            sub_arr.sort()
            if len(sub_arr) >= 1:
                tmp = sub_arr[1] - sub_arr[0]
                for idx in range(1,len(sub_arr)-1):
                    if tmp != sub_arr[idx+1] - sub_arr[idx]:
                        result.append(False)
                        break
                else:
                    result.append(True)
            else:
                result.append(True)
        return result
    
if __name__ == '__main__':
    sol = Solution()
    a = sol.checkArithmeticSubarrays([-12,-9,-3,-12,-6,15,20,-25,-20,-15,-10], [0,1,6,4,8,7], [4,4,9,7,9,10])
    # [false,true,false,false,true,true]
    print(a)