"""
You are given an integer array gifts denoting the number of gifts in various piles. Every second, you do the following:

- Choose the pile with the maximum number of gifts.
- If there is more than one pile with the maximum number of gifts, choose any.
- Leave behind the floor of the square root of the number of gifts in the pile. Take the rest of the gifts.

Return the number of gifts remaining after k seconds.
"""

"""
Example 1:

Input: gifts = [25,64,9,4,100], k = 4
Output: 29
Explanation: 
The gifts are taken in the following way:
- In the first second, the last pile is chosen and 10 gifts are left behind.
- Then the second pile is chosen and 8 gifts are left behind.
- After that the first pile is chosen and 5 gifts are left behind.
- Finally, the last pile is chosen again and 3 gifts are left behind.
The final remaining gifts are [5,8,9,4,3], so the total number of gifts remaining is 29.

Example 2:

Input: gifts = [1,1,1,1], k = 4
Output: 4
Explanation: 
In this case, regardless which pile you choose, you have to leave behind 1 gift in each pile. 
That is, you can't take any pile with you. 
So, the total gifts remaining are 4.
"""

import math
class Solution(object):
    def pickGifts(self, gifts, k):
        """
        :type gifts: List[int]
        :type k: int
        :rtype: int
        
        k번 반복해서 
        가장 큰 수의 제곱근만큼의 선물을 남겨둔다.
        마지막에 남은 선물을 확인
        """
        
        # 1. Sorting을 사용하는 방법
        for _ in range(k):
            gifts.sort(reverse=True) # 제일 큰 수를 앞으로 보내기 O(nLogn)
            gifts[0] = int(math.sqrt(gifts[0])) # 값을 제곱근 값으로 변경
        
        # 2. argmax를 사용하는 방법
        for _ in range(k):
            idx, gift = max(gifts)
        
        return sum(gifts)
        
        
if __name__=="__main__":
    sol = Solution()
    gifts_list = [[25,64,9,4,100], [1,1,1,1]]
    k_s = [4,4]
    
    for gifts, k in zip(gifts_list, k_s):
        print(sol.pickGifts(gifts,k))