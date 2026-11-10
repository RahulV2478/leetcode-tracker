# Last updated: 11/10/2026, 4:20:10 AM
1class Solution:
2    def subarraysDivByK(self, nums: list[int], k: int) -> int:
3        count = [0] * k
4        counter = 0
5        s = 0
6        count[0] = 1
7        
8        for num in nums:
9            s += num
10            mod = s % k
11            count[mod] += 1
12        
13        for i in range(len(count)):
14           if count[i] > 1:
15               
16                counter += (count[i] * (count[i] - 1) // 2)
17               
18        return counter