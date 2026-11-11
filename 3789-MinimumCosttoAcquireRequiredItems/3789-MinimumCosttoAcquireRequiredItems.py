# Last updated: 11/10/2026, 11:33:39 PM
1class Solution:
2    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
3        min_needed = min(need1, need2)
4        cost_for_both = min((cost1 + cost2), costBoth)
5        total_cost = 0
6        
7        total_cost += cost_for_both * min_needed
8        need1 -= min_needed
9        need2 -= min_needed
10
11        if need1 > 0:
12            cost = min(cost1, costBoth)
13            total_cost += cost * need1
14        if need2 > 0:
15            cost = min(cost2, costBoth)
16            total_cost += cost * need2
17        return total_cost
18