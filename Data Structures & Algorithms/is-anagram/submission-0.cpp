class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> s_frequencyMap;
        unordered_map<char, int> t_frequencyMap;

        for (const char& character: s){
            s_frequencyMap[character]++;
        }

        for (const char& character: t){
            t_frequencyMap[character]++;
        }

        if (s_frequencyMap == t_frequencyMap){
            return true;
        }
        else{
            return false;
        }
    }
};
