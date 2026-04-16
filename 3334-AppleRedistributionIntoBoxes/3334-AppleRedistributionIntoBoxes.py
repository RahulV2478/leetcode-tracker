# Last updated: 4/15/2026, 11:49:16 PM
class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort()
        apple_sum = sum(apple)
        counter = 0
        for i in range(len(capacity) - 1, -1, -1):
            if apple_sum <= 0:
                break
            apple_sum -= capacity[i]
            
            counter += 1
            
            
        return counter


