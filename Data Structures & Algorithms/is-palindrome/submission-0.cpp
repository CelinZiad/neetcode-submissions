class Solution {
public:
    bool isPalindrome(string s) {
        string alpha = "";
        for (char i : s){
            if (isalnum(i)){
                i = (char)tolower(i);
                alpha += i;
            }
        }
        for (char i : alpha){
            cout << i;
        }

        int j = alpha.size();
        j = j - 1;
        for (int i = 0; i < s.size()/2; i++){
            if (alpha[i]==alpha[j]){
                j--;
                continue;
            }
            else{
                return false;
            }
        }
        return true;
    }
};
