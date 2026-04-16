// Last updated: 4/15/2026, 11:49:37 PM

class Solution {
    public int maxFrequency(int[] nums, int k) {
        Arrays.sort(nums);
        int maxWindowLength = 1;
        long windowSum = 0;  // Use long to prevent overflow when summing
        int pointer1 = 0;
        
        for (int pointer2 = 1; pointer2 < nums.length; pointer2++) {
            // Calculate the operations needed to make the current window valid
            windowSum += (long)(nums[pointer2] - nums[pointer2 - 1]) * (pointer2 - pointer1);
            
            // If the total operations exceed k, shrink the window from the left
            while (windowSum > k) {
                windowSum -= nums[pointer2] - nums[pointer1];
                pointer1++;
            }
            
            // Update the maximum window length
            maxWindowLength = Math.max(maxWindowLength, pointer2 - pointer1 + 1);
        }
        
        return maxWindowLength;
    }
}
