class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string,vector<string>> sortedMap;

        for (string s : strs){
            string sorted = s;
            sort(sorted.begin(), sorted.end());
            if (sortedMap.contains(sorted)){
                sortedMap[sorted].push_back(s);
            }
            else{
                sortedMap[sorted] = {s};
            }
        }
        vector<vector<string>> result;
        for (const auto& [key, val] : sortedMap){
            result.push_back(val);
        }
        return result;

    }
};
