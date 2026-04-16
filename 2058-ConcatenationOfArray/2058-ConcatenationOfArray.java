// Last updated: 4/15/2026, 11:49:40 PM
class Solution {
    public int[] getConcatenation(int[] nums) {
        int array_len = nums.length;
        int[] newArr = new int[array_len * 2];
        for(int i = 0; i < nums.length; i++){
            newArr[i] = nums[i];
            newArr[i + nums.length] = nums[i];
        }
        return newArr;
    }
}