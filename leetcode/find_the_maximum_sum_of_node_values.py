# 3068. Find the Maximum Sum of Node Values

'''
There exists an undirected tree with n nodes numbered 0 to n - 1. You are given a 0-indexed 2D integer array edges of length n - 1, where edges[i] = [ui, vi] indicates that there is an edge between nodes ui and vi in the tree. You are also given a positive integer k, and a 0-indexed array of non-negative integers nums of length n, where nums[i] represents the value of the node numbered i.

Alice wants the sum of values of tree nodes to be maximum, for which Alice can perform the following operation any number of times (including zero) on the tree:

Choose any edge [u, v] connecting the nodes u and v, and update their values as follows:
nums[u] = nums[u] XOR k
nums[v] = nums[v] XOR k
Return the maximum possible sum of the values Alice can achieve by performing the operation any number of times.
'''

class Solution(object):
    def maximumValueSum(self, nums, k, edges):
        """
        :type nums: List[int]
        :type k: int
        :type edges: List[List[int]]
        :rtype: int
        """
        n = len(nums)
        xor_nums = list(map(lambda x : x^k, nums))
        results = 0
        cnt = 0
        gap = 99999999
        
        for i in range(n):
            if (xor_nums[i] > nums[i]):
                results += xor_nums[i]
                cnt += 1
            else:
                results += nums[i]
            
            gap = min(gap, abs(xor_nums[i]-nums[i]))

        if cnt % 2:
            results -= gap
                       
        return results
            
# 전체 합이 줄어들면 노드쌍 선택 x
# 늘어나면 선택 o 
        
        
if __name__== '__main__':
    sol = Solution()
    nums = [24,78,1,97,44]
    #      [30 72 7 103 42]
    k = 6
    edges = [[0,2],[1,2],[4,2],[3,4]]
    # test Case
    print(sol.maximumValueSum(nums,k,edges))