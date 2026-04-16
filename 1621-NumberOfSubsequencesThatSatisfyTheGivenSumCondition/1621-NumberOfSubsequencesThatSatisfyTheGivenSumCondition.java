// Last updated: 4/15/2026, 11:49:44 PM

class Solution {
    private static final int MOD = 1_000_000_007;

    public int numSubseq(int[] nums, int target) {
        Arrays.sort(nums);
        int pointer1 = 0;
        int pointer2 = nums.length - 1;
        int counter = 0;
        
        int[] power = new int[nums.length];
        power[0] = 1;
        for (int i = 1; i < nums.length; i++) {
            power[i] = (power[i - 1] * 2) % MOD;
        }

        while (pointer1 <= pointer2) {
            if (nums[pointer1] + nums[pointer2] <= target) {
                counter = (counter + power[pointer2 - pointer1]) % MOD;
                pointer1++;
            } else {
                pointer2--;
            }
        }
        return counter;
    }
}
