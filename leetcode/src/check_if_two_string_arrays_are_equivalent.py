# 1662. Check If Two String Arrays are Equivalent

'''
Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.

A string is represented by an array if the array elements concatenated in order forms the string.

'''

class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        return True if ''.join(word1) == ''.join(word2) else False


if __name__ == '__main__':
    sol = Solution()
    for word1,word2 in [[["ab", "c"],["a", "bc"]],[["a", "cb"],["ab", "c"]],[["abc", "d", "defg"],["abcddefg"]]]:
        print(sol.arrayStringsAreEqual(word1,word2))
        