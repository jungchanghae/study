# 78. Subsets


"""

Given an integer array nums of unique elements, return all possible 
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

"""

'''
Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
'''

class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        subsets = []
        for mask in range(1<<n):
            subset = []
            for i in range(n):
                if mask & (1<<i):
                    subset.append(nums[i])
            subsets.append(subset)
            
        return subsets
        

if __name__ == '__main__':
    sol = Solution()
    for nums in [[1,2,3],[0]]:
        print(sol.subsets(nums))