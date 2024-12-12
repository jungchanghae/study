# 2563. Count the Number of Fair Pairs

"""
Given a 0-indexed integer array nums of size n and two integers lower and upper, return the number of fair pairs.

A pair (i, j) is fair if:

- 0 <= i < j < n, and
- lower <= nums[i] + nums[j] <= upper

Example 1:

Input: nums = [0,1,7,4,4,5], lower = 3, upper = 6
Output: 6
Explanation: There are 6 fair pairs: (0,3), (0,4), (0,5), (1,3), (1,4), and (1,5).

Example 2:

Input: nums = [1,7,9,2,5], lower = 11, upper = 11
Output: 1
Explanation: There is a single fair pair: (2,3).

Note:

Sorting을 하고, 2진 탐색으로 들어가야 시간 복잡도를 줄이는데,,,
0 1 4 4 5 7 에서 음수도 있을 수 있다는 걸 감안하면... 단순히 현재 숫자가 크다는 이유로 브레이크는 불가능
시작부분부터 가운데를 기준으로 만족하는 개수를 양쪽으로 찾기
lower를 만족하는 부분의 index, upper를 만족하는 부분의 index를 찾아서 차이 구하기

"""

class Solution:
    def countFairPairs(self, nums, lower, upper):
        nums.sort()
        n = len(nums)
        result = 0
        for i in range(n):
            left = self.lower_bound(nums, i + 1, n - 1, lower - nums[i])
            right = self.upper_bound(nums, i + 1, n - 1, upper - nums[i])
            result += right - left + 1
        return result
    
    def lower_bound(self, nums, start, end, target):
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return start
    
    def upper_bound(self, nums, start, end, target):
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] <= target:
                start = mid + 1
            else:
                end = mid - 1
        return end

        
if __name__== '__main__':
    sol = Solution()
    # nums = [0,1,7,4,4,5]
    # lower = 3
    # upper = 6
    
    # nums = [1,7,9,2,5]
    # lower = 11
    # upper = 11
    
    nums = [0,0,0,0,0,0]
    lower = 0
    upper = 0
    # test Case
    print(sol.countFairPairs(nums,lower,upper))