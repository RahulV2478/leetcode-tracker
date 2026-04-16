# Last updated: 4/15/2026, 11:49:22 PM
class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        # use binary search on answer array to find answer
        # answers minimum is lowest y coordinate and max is highest y coordinate
        low = float('inf')
        high = float('-inf')
        for square in squares:
            low = min(low, square[1])
            high = max(high, (square[1] + square[2]))
        for i in range(60):
            mid = (low + high) / 2

            area_above, area_below = self.computeArea(mid, squares)
            if area_above > area_below:
                low = mid
            if area_below >= area_above:
                high = mid
        return mid
        
    def computeArea(self, mid, squares):
        area_above = 0
        area_below = 0

        for square in squares:
            if (square[1] >= mid):
                area_above += (square[2] ** 2)
            elif ((square[1] + square[2]) <= mid): 
                area_below += (square[2] ** 2)
            
            else:
                area_above += ((square[1] + square[2]) - mid) * square[2]
                area_below += (mid - square[1]) * square[2]
        return area_above, area_below
        