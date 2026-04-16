# Last updated: 4/15/2026, 11:49:24 PM
class Solution(object):
    def canMakeSubsequence(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: bool
        """
        pointer1 = 0
        for char in str1:
            if ord(char) - ord(str2[pointer1]) == 0 or ord(char) - ord(str2[pointer1]) == -1 or ord(char) - ord(str2[pointer1]) == 25:
                pointer1+=1
                if(pointer1 >= len(str2)):
                    return True
        return False

        