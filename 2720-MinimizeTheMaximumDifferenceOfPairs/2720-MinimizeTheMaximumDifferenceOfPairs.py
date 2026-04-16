# Last updated: 4/15/2026, 11:49:26 PM
from typing import List

class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()

        if p == 0:
            return 0

        differences = [nums[i] - nums[i - 1] for i in range(1, len(nums))]
        
        def canFormPairs(mid: int) -> bool:
            count = 0
            i = 0
            while i < len(nums) - 1:
                if nums[i+1] - nums[i] <= mid:
                    count += 1
                    i += 2  
                else:
                    i += 1  
                if count >= p: 
                    return True
            return count >= p

        low, high = 0, max(differences)  
        while low < high:
            mid = (low + high) // 2
            if canFormPairs(mid):
                high = mid  
            else:
                low = mid + 1  
        
        return low
