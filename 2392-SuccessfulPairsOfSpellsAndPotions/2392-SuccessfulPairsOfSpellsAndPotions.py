# Last updated: 4/15/2026, 11:49:31 PM
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        result = []
        potions.sort()
        for spell in spells:
            counter = 0
            low = 0
            high = len(potions) - 1
            while(low <= high):
                mid = (low + high) // 2
                
                if(spell * potions[mid] >= success):

                    counter = len(potions) - mid
                    high = mid - 1
                else:
                    low = mid + 1
            result.append(counter)
        return result