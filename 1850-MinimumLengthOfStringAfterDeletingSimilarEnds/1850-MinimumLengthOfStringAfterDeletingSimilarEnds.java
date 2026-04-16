// Last updated: 4/15/2026, 11:49:39 PM
class Solution {
    public int minimumLength(String s) {
        int pointer1 = 0;
        int pointer2 = s.length() - 1;

        while (pointer1 < pointer2 && s.charAt(pointer1) == s.charAt(pointer2)) {
            char letter = s.charAt(pointer1);
            
            while (pointer1 <= pointer2 && s.charAt(pointer1) == letter) {
                pointer1++;
            }
            
            while (pointer1 <= pointer2 && s.charAt(pointer2) == letter) {
                pointer2--;
            }
        }

        return pointer2 - pointer1 + 1;
    }
}
