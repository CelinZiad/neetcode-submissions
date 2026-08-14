class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int begin = 0;
        int end = numbers.size() - 1;
        bool continu = true;
        while(continu){
            int attempt = numbers[begin] + numbers[end];
            if (attempt==target){
                continu = false;
                return {begin+1, end+1};
            }
            if (attempt > target){
                end--;
            }
            if (attempt < target){
                begin++;
            }
        }
    }
};
