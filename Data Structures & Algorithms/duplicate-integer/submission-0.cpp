class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::unordered_map<int, int> noDuplicates;

        for (const int& key : nums){
            noDuplicates[key] = 1;
        }
        if (nums.size()!=noDuplicates.size()){
            return true;
        }
        else{
            return false;
        }
    }
};