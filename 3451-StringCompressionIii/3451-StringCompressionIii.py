# Last updated: 4/15/2026, 11:49:17 PM
class Solution:
    def compressedString(self, word: str) -> str:
        counter = 0
        result = []
        for index, char in enumerate(word):
            if(index == 0 or (word[index] == word[index - 1] and counter < 9)):
                counter+=1
            else:
                result.append(str(counter))
                result.append(word[index - 1])
                counter = 1
        result.append(str(counter))
        result.append(word[-1])
        return ''.join(result)
                