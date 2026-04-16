# Last updated: 4/15/2026, 11:49:33 PM
class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        max_q = max(quantities)
        
        low = 1  
        high = max_q  
        
        while low <= high:
            mid = (low + high) // 2
            req_store = 0
            for q in quantities:
                req_store += (q + mid - 1) // mid  
            
            if req_store <= n:
                high = mid - 1
            else:
                low = mid + 1
                    
        return low  