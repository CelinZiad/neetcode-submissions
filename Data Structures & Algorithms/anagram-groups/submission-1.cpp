class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<std::string>> anagramMap = {};
        string temp;
        for (int i = 0;i<strs.size();i++){
            temp = strs[i];
            sort(temp.begin(), temp.end());
            anagramMap[temp].push_back(strs[i]);
        }

        vector<vector<string>> result;
        while (!anagramMap.empty()){
            result.push_back((*anagramMap.begin()).second);
            //begin is an iterator. anagramMap.begin() = ptr | *anagramMap.begin() = value
            //second = value of hashmap
            anagramMap.erase(anagramMap.begin());
        }
        return result;
    }
};

/*

logic:
for loop in strs
string temp = sorted element in strs
hashmap initialized where key = sorted element and value = list of element
if temp not in hashmap, key = temp, value = strs[i]
if temp in hashmap, add strs[i] to value



*/
