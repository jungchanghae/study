# 1160. Find Words That Can Be Formed by Characters

'''
You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words.
'''

class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        result=0
        for i in range(len(words)):
            chars_spell = list(chars)
            for k in list(words[i]):
                if k in chars_spell:
                    chars_spell.remove(k)
                else:
                    break
            else:
                result += len(words[i])
        return result
    
    
if __name__ == '__main__':
    sol = Solution()
    for words, chars in [[["cat","bt","hat","tree"], "atach"],[["hello","world","leetcode"],"welldonehoneyr"]]:
        print(sol.countCharacters(words,chars))