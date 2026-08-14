class Solution {
public:
    bool isValid(string s) {
        stack<char> brackets;
        for (char i : s){
            if (brackets.empty() && (i == ')' || i == '}' || i == ']')){
                brackets.push(i);
            }
            else{
            if (i == '(' || i == '{' || i == '['){
                brackets.push(i);
            }
            else{
                if ((i == ')' && brackets.top()=='(') || (i == '}' && brackets.top()=='{') || (i == ']' && brackets.top()=='[')){
                    brackets.pop();
                }
                else{
                    brackets.push(i);
                }
            }
            }
        }
        if (brackets.empty()){
            return true;
        }
        else{
            return false;
        }
    }
};
