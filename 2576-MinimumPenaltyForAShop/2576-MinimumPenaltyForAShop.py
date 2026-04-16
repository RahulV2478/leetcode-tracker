# Last updated: 4/15/2026, 11:49:29 PM
class Solution:
    def bestClosingTime(self, customers: str) -> int:
        y_count = 0
        n_count = 0
        for customer in customers:
            if customer == "Y":
                y_count += 1
        min_val = y_count
        min_idx = 0
        for idx in range(len(customers)):
            if customers[idx] == "Y":
                y_count -= 1
            if customers[idx] == "N":
                n_count += 1
            if (y_count + n_count) < min_val:
                min_val = y_count + n_count
                min_idx = idx + 1
        return min_idx
  
        
