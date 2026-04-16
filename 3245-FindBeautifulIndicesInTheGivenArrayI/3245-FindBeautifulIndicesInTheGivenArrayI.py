# Last updated: 4/15/2026, 11:49:20 PM
class Solution(object):
    def beautifulIndices(self, s, a, b, k):
        """
        :type s: str
        :type a: str
        :type b: str
        :type k: int
        :rtype: List[int]
        """
        a_indices = []
        b_indices = []
        for i in range(0, (len(s) - len(a) + 1)):
            if s[i:i+len(a)] == a:
                a_indices.append(i)
        for j in range(0, (len(s) - len(b) + 1)):
            if s[j:j+len(b)] == b:
                b_indices.append(j)
        result = []
        a_pointer = 0
        b_pointer = 0
        while a_pointer < len(a_indices) and b_pointer < len(b_indices):
            total = a_indices[a_pointer] - b_indices[b_pointer]
            if total <= k and total * -1 <= k:
                result.append(a_indices[a_pointer])
                a_pointer += 1
            elif a_indices[a_pointer] > b_indices[b_pointer]:
                b_pointer += 1
            else:
                a_pointer += 1
        return result
