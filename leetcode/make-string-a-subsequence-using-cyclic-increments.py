#2825. Make String a Subsequence Using Cyclic Increments

'''
You are given two 0-indexed strings str1 and str2.

In an operation, you select a set of indices in str1, and for each index i in the set, increment str1[i] to the next character cyclically. That is 'a' becomes 'b', 'b' becomes 'c', and so on, and 'z' becomes 'a'.

Return true if it is possible to make str2 a subsequence of str1 by performing the operation at most once, and false otherwise.

Note: 
A subsequence of a string is a new string that is formed from the original string by deleting some (possibly none) of the characters without disturbing the relative positions of the remaining characters.
'''

class Solution(object):
    def canMakeSubsequence(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: bool
        """
        def next_alpha(s):
            return chr((ord(s)+1 - 97) % 26 + 97)
        
        if len(str1) < len(str2):
            return False
        
        idx, n = 0, len(str2)
        for s in str1:
            if idx == n: 
                break
            
            if s == str2[idx]:
                idx += 1
                continue
            
            if str2[idx] == next_alpha(s):
                idx += 1
                
        return idx == n    
        
        
if __name__=='__main__':
    sol = Solution()
    
    example = [['abc','ad'],['zc','ad'],['ab','d']]
    
    for e in example:
        print(sol.canMakeSubsequence(e[0],e[1]))