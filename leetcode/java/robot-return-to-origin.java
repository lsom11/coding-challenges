class Solution {
    public boolean judgeCircle(String moves) {
        if(moves.length() % 2 != 0) return false;
        int f = 0;
        int s = 0;

        for(char c: moves.toCharArray()) {
            if(c == 'U') f++;
            if(c == 'D') f--;
            if(c == 'L') s++;
            if(c == 'R') s--;
        }

        return (f==0) && (s==0);
    }
}