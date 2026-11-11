# Last updated: 11/10/2026, 11:56:14 PM
1class Solution:
2    def climbStairs(self, n: int, costs: List[int]) -> int:
3        if n == 0:
4            return 0
5        dp = [0] * (n + 1)
6        dp[1] = 1 + costs[0]
7        if n == 1:
8            return dp[1]
9        dp[2] = min(1 + dp[1] + costs[1], 4 + costs[1])
10        for i in range(3, n + 1):
11
12            dp[i] = min((dp[i - 3] + 9), (dp[i-2] + 4), (dp[i - 1] + 1)) + costs[i - 1]
13        return dp[-1]
14        
15
16
17