# Last updated: 4/15/2026, 11:49:19 PM
class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        first_num = nums[0]
        nums.pop(0)
        nums.sort()
        return first_num + nums[0] + nums[1]