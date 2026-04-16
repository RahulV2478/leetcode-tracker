// Last updated: 4/15/2026, 11:49:43 PM
class Solution {
    public int minCost(String colors, int[] neededTime) {
        int pointer1 = 0;
        int pointer2 = 1;
        int maxValue = 0;
        int result = 0;
        while(pointer2 < colors.length()){
            if(colors.charAt(pointer1) != colors.charAt(pointer2)){
                pointer1 = pointer2;
                maxValue = 0;
            }else{
                if(maxValue == 0){
                    maxValue = neededTime[pointer1];
                }
                if(neededTime[pointer2] >= maxValue){
                    result += maxValue;
                    maxValue = neededTime[pointer2];
                }else{
                    result+=neededTime[pointer2];
                }
            }
            pointer2++;
        }
        return result;
    }
}