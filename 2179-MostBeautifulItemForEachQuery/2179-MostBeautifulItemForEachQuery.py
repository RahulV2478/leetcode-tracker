# Last updated: 4/15/2026, 11:49:34 PM
class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        newList = sorted(items, key=lambda x: x[0])
        result = []
        currMax = 0
        for x in newList:
            if(x[1] > currMax):
                currMax = x[1]
            else:
                x[1] = currMax    
        print(newList)
        for query in queries:
            low, high = 0, len(newList) - 1
            maxBeauty = 0  

            while low <= high:
                mid = (low + high) // 2
                if newList[mid][0] <= query:  
                    maxBeauty = newList[mid][1]  
                    low = mid + 1  
                else:
                    high = mid - 1  

            
            result.append(maxBeauty)
        return result
            
            

    
            

        