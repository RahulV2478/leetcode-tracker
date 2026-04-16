// Last updated: 4/15/2026, 11:49:43 PM
class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        vector<int> myVector(nums.size() * 2, 0);
        for (int i = 0; i < nums.size(); ++i) {
            myVector[i] = nums[i];       // First copy
            myVector[i + nums.size()] = nums[i];   // Second copy
        }
        cout << endl;
        return myVector;  

    }
};