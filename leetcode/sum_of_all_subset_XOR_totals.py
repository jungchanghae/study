# 1863. Sum of All Subset XOR Totals

'''
The XOR total of an array is defined as the bitwise XOR of all its elements, or 0 if the array is empty.

For example, the XOR total of the array [2,5,6] is 2 XOR 5 XOR 6 = 1.
Given an array nums, return the sum of all XOR totals for every subset of nums. 

Note: Subsets with the same elements should be counted multiple times.

An array a is a subset of an array b if a can be obtained from b by deleting some (possibly zero) elements of b.
'''

class Solution:
    def generate_subset(self, nums, index, subset, subsets):
        if len(nums) == index:
            subsets.append(subset[:])
            return subsets
        
        subset.append(nums[index])
        subsets = self.generate_subset(nums, index+1, subset, subsets)
        subset.pop()
        
        subsets = self.generate_subset(nums, index+1, subset, subsets)
        return subsets
    
    def subsetXORSum(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]

        subsets = self.generate_subset(nums, 0, [], [])
        
        result = 0
        for subset in subsets:
            subset_sum = 0
            for num in subset:
                subset_sum ^= num
            result += subset_sum         
        return result

if __name__ == '__main__':
    sol = Solution()
    for n in [[1,3],[5,1,6],[3,4,5,6,7,8]]:
        print(sol.subsetXORSum(n))
    # 6, 28, 480