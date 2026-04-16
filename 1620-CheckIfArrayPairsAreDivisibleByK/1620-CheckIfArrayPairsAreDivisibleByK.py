# Last updated: 4/15/2026, 11:49:45 PM
class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        mod = []
        s = {}
        for i in arr:
            mod.append(i % k)
        for j in mod:
            val = (k-j) % k
            
            if val in s:
                s[val]-=1
                if(s[val] == 0):
                    del s[val]
            else:
                if(j in s):
                    s[j] += 1
                else:
                    s[j] = 1
        if(s):
            return False
        else:
            return True
                    

            