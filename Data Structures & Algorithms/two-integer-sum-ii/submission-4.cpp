class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int begin = 0;
        int end = numbers.size() - 1;
        while(begin<end){
            int attempt = numbers[begin] + numbers[end];
            if (attempt==target){
                return {begin+1, end+1};
            }
            else if (attempt > target){
                end--;
            }
            else if (attempt < target){
                begin++;
            }
        }
        return {};
    }
};
