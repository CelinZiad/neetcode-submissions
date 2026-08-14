class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> freqMap;
        for (int i = 0; i<nums.size(); ++i){
            int check = target - nums[i];
            if (freqMap.contains(check)){
                return {freqMap[check], i};
            }
            freqMap[nums[i]] = i;

        }
        return {};

    }
};
