// Last updated: 4/15/2026, 11:49:41 PM
class Solution {
    public int minOperations(int[] nums, int x) {
        int sum = 0, winSum = 0, maxWinLen = -1;
        for(int i = 0; i < nums.length; i++) sum += nums[i];
        if (sum == x) return nums.length;
        for(int target = sum - x, pointer1 = 0, pointer2 = 0; pointer2 < nums.length; pointer2++){
            winSum += nums[pointer2];
            while(pointer1 <= pointer2 && winSum > target) winSum -= nums[pointer1++];
            if(winSum == target) maxWinLen = Math.max(maxWinLen, pointer2 - pointer1 + 1);
        }
        return (maxWinLen == -1) ? -1 : nums.length - maxWinLen;
    }
}