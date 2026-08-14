class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> frequencyMap = {};
        for (int i = 0; i<nums.size();i++){
            if (frequencyMap.contains(nums[i])){
                frequencyMap[nums[i]] = ++frequencyMap[nums[i]];
                //cout << "key: " << nums[i] << " value:" << frequencyMap[nums[i]] << endl;
            }
            else{
                frequencyMap[nums[i]] = 1;
                //cout << "key: " << nums[i] << " value:" << frequencyMap[nums[i]] << endl;
            }
        }
        
        vector<int> result;

        for (const auto& hash : frequencyMap){
           // cout << "size of result: " << result.size() << endl;
            if (result.size()<k){
                //cout << "size is under k" << endl;
                result.push_back(hash.first);
                //cout << "added to result: " << hash.first << endl;
            }
            else{
                int lowestIndex = 0;
                for (int i = 1; i < result.size(); i++){
                    if(frequencyMap[result[i]]<frequencyMap[result[lowestIndex]]){
                        lowestIndex = i;
                    }
                }
                if(frequencyMap[result[lowestIndex]]<hash.second){
                    result[lowestIndex] = hash.first;
                }
                sort(result.begin(), result.end());
            }
        }
        return result;
    }
};

/*
LOGIC:

1- create hashmap
2- key = element in nums, value = number of times it appears
3- sort map
4- take top k values
*/