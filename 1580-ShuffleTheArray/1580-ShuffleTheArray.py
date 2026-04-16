# Last updated: 4/15/2026, 11:49:46 PM
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = [0] * len(nums)
        for i in range(len(nums) // 2):
            print(i)
            result[i * 2] = nums[i]
            increment = i + (len(nums) // 2)
            result[i*2+1] = nums[increment]
        return result
