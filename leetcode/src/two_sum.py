# 1 Two Sum

"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""

'''
빠른 연산을 위해서 dict로 변환한 후,
앞에서부터 target을 빼고, 남은 수를 찾는다. (dict의 get은 O(1)이므로 전체는 O(n))
정답은 무조건 하나이므로, 같은 숫자가 답인 경우에는 앞의 index에서 검색했을 때 답이 나온다.
즉, dict로 설정해도 겹치는 수에 대해서 상관없다.
'''

class Solution:
    def twoSum(self, nums, target: int):
        nums_dict = {}
        for i, num in enumerate(nums):
            nums_dict[num] = i
        
        for fist_idx, num in enumerate(nums):
            complement = target - num
            second_idx = nums_dict.get(complement)
            if second_idx and fist_idx != second_idx:
                return [fist_idx, second_idx]    

if __name__=="__main__":
    sol = Solution()
    nums = [3,3]
    target = 6
    print(sol.twoSum(nums, target))