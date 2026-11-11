# Last updated: 11/10/2026, 11:40:37 PM
1class Solution:
2    def climbStairs(self, n: int) -> int:
3        if n == 1:
4            return 1
5        elif n == 2:
6            return 2
7        dp = [0] *  (n + 1)
8
9        dp[1] = 1
10        dp[2] = 2
11        for i in range(3, n + 1):
12            dp[i] = dp[i - 1] + dp[i - 2]
13        return dp[-1]
14
15