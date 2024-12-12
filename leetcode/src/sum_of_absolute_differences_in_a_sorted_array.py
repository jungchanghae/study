# 1685. Sum of Absolute Differences in a Sorted Array
'''
You are given an integer array nums sorted in non-decreasing order.

Build and return an integer array result with the same length as nums such that result[i] is equal to the summation of absolute differences between nums[i] and all the other elements in the array.

In other words, result[i] is equal to sum(|nums[i]-nums[j]|) where 0 <= j < nums.length and j != i (0-indexed).
'''

class Solution(object):
    def getSumAbsoluteDifferences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        result = [0]*n
        part_sum = [0]*n
        part_sum[0] = nums[0]
        for i in range(1,n):
            part_sum[i] = part_sum[i-1] + nums[i]
        
        for i in range(n):
            left = part_sum[i]
            rigth = part_sum[n-1] - part_sum[i]
            result[i] = abs(nums[i]*(i+1) - left) + abs(nums[i]*(n-i-1) - rigth)
        return result
        # return [sum([abs(num - nums[j]) for j in range(len(nums))]) for num in nums] # time out

if __name__ == '__main__':
    sol = Solution()
    for nums in [[2,3,5], [1,4,6,8,10]]:
        result = sol.getSumAbsoluteDifferences(nums)
        print(result)
        '''
        [4, 3, 5]
        [24, 15, 13, 15, 21]
        '''