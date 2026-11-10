# Last updated: 11/10/2026, 4:19:29 AM
1class Solution:
2    def subarraysDivByK(self, nums: list[int], k: int) -> int:
3        count = [0] * k
4        counter = 0
5        s = 0
6        prefix = []
7        count[0] = 1
8        def get_fibonacci_number(n):
9            if n == 0:
10                return 0
11            elif n == 1:
12                return 1
13
14            a, b = 0, 1
15            for _ in range(2, n + 1):
16                a, b = b, a + b  # Update 'a' and 'b' to move to the next pair
17
18            return b
19
20        for num in nums:
21            s += num
22            mod = s % k
23            prefix.append(mod)
24            count[mod] += 1
25        
26        print(count)
27        for i in range(len(count)):
28           if count[i] > 1:
29               
30                counter += (count[i] * (count[i] - 1) // 2)
31            
32        
33               
34        return counter