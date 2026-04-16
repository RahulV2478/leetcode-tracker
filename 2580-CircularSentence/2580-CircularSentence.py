# Last updated: 4/15/2026, 11:49:29 PM
class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split()
        for index, word in enumerate(words):
            if index == 0:
                continue
            else:
                word_to_check = words[index - 1]
                if word[0] != word_to_check[-1]:
                    return False
        return words[0][0] == words[-1][-1]