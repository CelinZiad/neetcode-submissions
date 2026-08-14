class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<Character, Integer> s_map = new HashMap<>();
        HashMap<Character, Integer> t_map = new HashMap<>();
        
        for (char key : s.toCharArray()) {
            if (s_map.containsKey(key)){
                s_map.put(key, s_map.get(key)+1);
            }
            else{
                s_map.put(key, 1);
            }
        }
        for (char key : t.toCharArray()) {
            if (t_map.containsKey(key)){
                t_map.put(key, t_map.get(key)+1);
            }
            else{
                t_map.put(key, 1);
            }
        }
        return s_map.equals(t_map);
    }
}
