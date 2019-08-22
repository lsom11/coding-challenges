class Solution {
    public String toLowerCase(String str) {

        StringBuilder sb = new StringBuilder();

        char c = ' ';
        for (int i = 0; i < str.length(); i++) {
            int j = (str.charAt(i) - 'A');
            if (j > -1 && j < 27) {
                c = (char) (j + 97);
            } else {
                c = str.charAt(i);
            }
            sb.append("" + c);
        }

        return sb.toString();
    }
}