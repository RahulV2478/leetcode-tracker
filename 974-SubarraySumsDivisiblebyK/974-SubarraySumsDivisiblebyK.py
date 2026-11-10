# Last updated: 11/10/2026, 4:20:03 AM
1class Solution:
2    def subarraysDivByK(self, nums: list[int], k: int) -> int:
3        count = [0] * k
4        counter = 0
5        s = 0
6        prefix = []
7        count[0] = 1
8        
9        for num in nums:
10            s += num
11            mod = s % k
12            prefix.append(mod)
13            count[mod] += 1
14        
15        for i in range(len(count)):
16           if count[i] > 1:
17               
18                counter += (count[i] * (count[i] - 1) // 2)
19            
20        
21               
22        return counter