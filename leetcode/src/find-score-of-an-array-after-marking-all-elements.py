# 2593
"""
You are given an array nums consisting of positive integers.

Starting with score = 0, apply the following algorithm:

- Choose the smallest integer of the array that is not marked. If there is a tie, choose the one with the smallest index.
- Add the value of the chosen integer to score.
- Mark the chosen element and its two adjacent elements if they exist.
- Repeat until all the array elements are marked.

Return the score you get after applying the above algorithm.
"""

"""
1. 마킹되지 않은 가장 작은 값을 찾고 score에 더한다.(같은 값일 경우 index가 작은거)
2. 그 값과 그 양 옆의 값을 marking한다.
3. 위를 반복하면서 모든 값이 마킹시킨다.
"""

class Solution(object):
    def findScore(self, nums:list) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        score = 0
        len_nums = len(nums)
        marked_list = set() # marked idx를 넣기 위함
        idx_list = [(nums[idx], idx) for idx in range(len_nums)]
        idx_list.sort(key=lambda x: (x[0],x[1]))
        score = 0
        
        for val, idx in idx_list:
            if idx not in marked_list:
                score += val
                marked_list.add(idx)
                marked_list.add(idx-1)
                marked_list.add(idx+1)
                
        return score
    
if __name__ == '__main__':
    sol = Solution()
    nums_list = [[2,1,3,4,5,2], [2,3,5,1,3,2], [10,44,10,8,48,30,17,38,41,27,16,33,45,45,34,30,22,3,42,42]]
    
    for nums in nums_list:
        print(sol.findScore(nums))