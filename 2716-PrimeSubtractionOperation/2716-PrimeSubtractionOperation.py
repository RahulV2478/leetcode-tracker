# Last updated: 4/15/2026, 11:49:27 PM
from typing import List

class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        n = max(nums)  
        
        primes = [True] * (n + 1)
        primes[0], primes[1] = False, False  

        for p in range(2, int(n**0.5) + 1):
            if primes[p]:
                for i in range(p * p, n + 1, p):
                    primes[i] = False

        pn = [p for p, is_prime in enumerate(primes) if is_prime]
        
        for i in range(len(nums)):
            low, high = 0, len(pn) - 1
            lowestAcceptableVal = 1000000000  
            
            while low <= high:
                mid = (low + high) // 2
                candidate_prime = pn[mid]
                
                if (i == 0 and candidate_prime < nums[i]) or (i > 0 and nums[i] - candidate_prime > nums[i - 1]):
                    lowestAcceptableVal = candidate_prime  
                    low = mid + 1  
                else:
                    high = mid - 1  
        
            if lowestAcceptableVal != 1000000000:
                nums[i] -= lowestAcceptableVal

        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                return False
        return True
