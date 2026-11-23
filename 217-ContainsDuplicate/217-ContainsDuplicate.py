# Last updated: 11/23/2026, 3:20:29 PM
1class Solution:
2    def containsDuplicate(self, nums: list[int]) -> bool:
3        s = set()
4        for num in nums:
5            if num in s:
6                return True
7            s.add(num)
8        return False