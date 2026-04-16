# Last updated: 4/15/2026, 11:49:47 PM
class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        result = prices[:]
        stack = []
        for i in range(len(prices)):
            while stack and prices[i] <= prices[stack[-1]]:
                idx = stack.pop()
                result[idx] -= prices[i]
            stack.append(i)
        return result
                    
            
