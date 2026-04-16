// Last updated: 4/15/2026, 11:49:32 PM
class Solution {
    public int[] rearrangeArray(int[] nums) {
        int posCount = 0;
        int negCount = 0;
        int[] transformed = new int[nums.length];
        for(int i = 0; i < nums.length; i++){
            if(nums[i] >= 0){
                transformed[posCount * 2] = nums[i];
                posCount++;
            }else{
                transformed[negCount * 2 + 1] = nums[i];
                negCount++;
            }
        }
        for(int j = 0; j < transformed.length; j++){
            nums[j] = transformed[j];
        }
        return nums;
    }
}