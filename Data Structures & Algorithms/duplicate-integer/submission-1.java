class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashMap<Integer, Integer> map = new HashMap<>();

        for (Integer key : nums){
            map.put(key, 0);
        }

        if (nums.length != map.size()){
            return true;
        }
        else{
            return false;
        }
    }
}