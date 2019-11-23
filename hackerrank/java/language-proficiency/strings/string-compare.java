import java.util.Scanner;

public class Solution {

    public static String getSmallestAndLargest(String s, int k) {
        String smallest = s.substring(0, k);
        String largest = s.substring(0, k);
        for (int i = 0; i <= s.length() - k; i++) {
            String substr = s.substring(i, i + k);
            if (substr.compareTo(smallest) < 0) {
                smallest = substr;
            } else if (substr.compareTo(largest) > 0) {
                largest = substr;
            }
        }   
        
        return smallest + "\n" + largest;
    }
