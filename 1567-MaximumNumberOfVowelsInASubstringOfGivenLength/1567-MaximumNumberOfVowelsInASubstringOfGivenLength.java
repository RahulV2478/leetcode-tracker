// Last updated: 4/15/2026, 11:49:47 PM
class Solution {
    public int maxVowels(String s, int k) {
        int vowelCounter = 0;
        String vowels = "aeiou";
        int max = 0;
        int pointer1 = 0;
        for(int pointer2 = 0; pointer2 < s.length(); pointer2++){
            if(pointer2 < k){
                char letter = s.charAt(pointer2);
                if(vowels.indexOf(letter) != -1){
                    vowelCounter++;
                }
            }else{
                if(vowels.indexOf(s.charAt(pointer1)) != -1){
                    vowelCounter--;
                }
                
                if(vowels.indexOf(s.charAt(pointer2)) != -1){
                    
                    vowelCounter++;
                }
                pointer1++;

            }
            
            if(vowelCounter > max){
                max = vowelCounter;
            }
            
        }
        return max;
    }
}