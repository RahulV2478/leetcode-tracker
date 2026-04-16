# Last updated: 4/15/2026, 11:49:36 PM
class Solution(object):
    def mergeTriplets(self, triplets, target):
        """
        :type triplets: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        found = [False, False, False]
        for triplet in triplets:
            if target[0] >= triplet[0] and target[1] >= triplet[1] and target[2] >= triplet[2]:
                for idx in range(len(triplet)):
                    if target[idx] == triplet[idx]:
                        found[idx] = True
        return all(found)
                        
                
            
                    
        