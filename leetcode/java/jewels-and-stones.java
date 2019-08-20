import java.util.HashMap;

class Solution {
    public int numJewelsInStones(String J, String S) {
        int count = 0;
        HashMap<Character, Integer> map = new HashMap<Character, Integer>();

        for (int i = 0; i < S.length(); i++) {
            char c = S.charAt(i);
            int total = map.containsKey(c) ? map.get(c) + 1 : 1;
            map.put(c, total);
        }

        for (int i = 0; i < J.length(); i++) {
            char c = J.charAt(i);
            boolean inMap = map.containsKey(c);
            if (inMap) {
                int keyCount = map.get(c);
                count += keyCount;
            }
        }

        return count;
    }
}