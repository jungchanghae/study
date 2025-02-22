# 2461. Maximum Sum of Distinct Subarrays With Length K

"""
You are given an integer array nums and an integer k. Find the maximum subarray sum of all the subarrays of nums that meet the following conditions:

The length of the subarray is k, and
All the elements of the subarray are distinct.
Return the maximum subarray sum of all the subarrays that meet the conditions. If no subarray meets the conditions, return 0.

A subarray is a contiguous non-empty sequence of elements within an array.
"""

'''
window sliding하면서 각 list에 겹치는게 있는지 확인 후 없으면 합친다. 이전 max와 비교해서 크면 저장
'''

from collections import defaultdict

class Solution:
    def maximumSubarraySum(self, nums: list, k: int) -> int:
        count_dict = defaultdict(int)
        maximum_sum = 0 # 모든 값이 양수이므로 항상 0보단 큼
        cur_sum = 0

        for i, num in enumerate(nums[:k]):
            count_dict[num] += 1
            cur_sum += num

        if max(count_dict.values()) < 2:
            maximum_sum = cur_sum
            
        for idx in range(k,len(nums)):
            count_dict[nums[idx-k]] -= 1
            count_dict[nums[idx]] += 1
            
            cur_sum += nums[idx] - nums[idx-k]
            if count_dict[nums[idx-k]] == 0:
                del count_dict[nums[idx-k]]
            if len(count_dict) == k:
                maximum_sum = max(cur_sum, maximum_sum)
                
        return maximum_sum
        
if __name__=='__main__':
    sol = Solution()
    
    example = [17,13,17,20,5,18,5,6]
    k = 6
    
    print(sol.maximumSubarraySum(example,k))