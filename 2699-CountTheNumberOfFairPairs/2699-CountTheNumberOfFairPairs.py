# Last updated: 4/15/2026, 11:49:28 PM
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        counter = 0
        n = len(nums)
        
        for i in range(n):
            left = i + 1
            right = n - 1
            
            while left <= right:
                mid = (left + right) // 2
                if nums[i] + nums[mid] >= lower:
                    right = mid - 1
                else:
                    left = mid + 1
            start = left
            
            left = i + 1
            right = n - 1
            
            while left <= right:
                mid = (left + right) // 2
                if nums[i] + nums[mid] <= upper:
                    left = mid + 1
                else:
                    right = mid - 1
            end = right
            
            if start <= end:
                counter += end - start + 1
        
        return counter


