# Last updated: 4/15/2026, 11:49:39 PM
class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        word1list, word2list = list(word1), list(word2)
        result = []
        shorter_word = word1list if len(word1list) < len(word2list) else word2list
        longer_word = word1list if len(word1list) > len(word2list) else word2list
        idx = 0
        while idx < len(shorter_word):
            result.append(word1[idx])
            result.append(word2[idx])
            idx += 1
        while idx < len(longer_word):
            result.append(longer_word[idx])
            idx += 1
        

        return ''.join(result)

        