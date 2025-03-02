# 2570. Merge Two 2D Arrays by Summing Values

"""
You are given two 2D integer arrays nums1 and nums2.

- nums1[i] = [id_i, val_i] indicate that the number with the id id_i has a value equal to val_i.
- nums2[i] = [id_i, val_i] indicate that the number with the id id_i has a value equal to val_i.

Each array contains unique ids and is sorted in ascending order by id.

Merge the two arrays into one array that is sorted in ascending order by id, respecting the following conditions:

- Only ids that appear in at least one of the two arrays should be included in the resulting array.
- Each id should be included only once and its value should be the sum of the values of this id in the two arrays. If the id does not exist in one of the two arrays, then assume its value in that array to be 0.

Return the resulting array. The returned array must be sorted in ascending order by id.
"""
from typing import List

'''
set id와 list index를 매핑하는 dict를 구성해서 필요한 index만을 사용한다.
같은 O(n)이긴 하나, 아래보다 빠름
'''

class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        
        # id의 값들을 가지고 set을 만들기
        set_id = set()
        for n1_id, _ in nums1:
            set_id.add(n1_id)
        for n2_id, _ in nums2:
            set_id.add(n2_id)
        set_id = sorted(set_id)
        
        # id-index dict만들기
        dict_ids = dict()
        for idx, n_id in enumerate(set_id):
            dict_ids[n_id] = idx

        results = []        
        for id in set_id:
            results.append([id,0])
            
        # nums1의 값들 더하기
        for n1_id, n1_val in nums1:
            results[dict_ids[n1_id]][1] += n1_val
        
        # nums2의 값들 더하기
        for n2_id, n2_val in nums2:
            results[dict_ids[n2_id]][1] += n2_val
    
        return results

# '''
# nums1의 원소들을 이용해서 하나의 리스트를 만들고,
# 그 리스트에 nums2의 원소를 더하는 방식
# 이후 val이 0이 아닌 것들을 반환한다.
# O(n)
# '''

# class Solution:
#     def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
#         """
#         python은 idx가 0부터 이므로 그 부분을 생각하며 작성
#         """
#         max_idx = max(self.maximum_index(nums1), self.maximum_index(nums2))
#         results_temp = []
#         results = []
        
#         for i in range(1, max_idx+1):
#             results_temp.append([i,0])
            
#         # nums1의 값들 더하기
#         for n1_id, n1_val in nums1:
#             results_temp[n1_id-1][1] += n1_val
        
#         # nums2의 값들 더하기
#         for n2_id, n2_val in nums2:
#             results_temp[n2_id-1][1] += n2_val
        
#         for id, val in results_temp:
#             if val != 0:
#                 results.append([id,val])
        
#         return results
    
#     def maximum_index(self, nums: List[List[int]]) -> int:
#         """
#         각 list의 index 중 가장 큰 값을 찾는다.
#         """
#         max_idx = 0
#         for idx, val in nums:
#             if idx >= max_idx:
#                 max_idx = idx
#         return max_idx
    
if __name__=='__main__':
    
    sol = Solution()
    
    nums1 = [[148,597],[165,623],[306,359],[349,566],[403,646],[420,381],[566,543],[730,209],[757,875],[788,208],[932,695]]
    nums2 = [[74,669],[87,399],[89,165],[99,749],[122,401],[138,16],[144,714],[148,206],[177,948],[211,653],[285,775],[309,289],[349,396],[386,831],[403,318],[405,119],[420,153],[468,433],[504,101],[566,128],[603,688],[618,628],[622,586],[641,46],[653,922],[672,772],[691,823],[693,900],[756,878],[757,952],[770,795],[806,118],[813,88],[919,501],[935,253],[982,385]]
    
    print(sol.mergeArrays(nums1, nums2))