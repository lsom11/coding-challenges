import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {



    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        int n = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");
        int current_ones = 0;
        int max_ones = 0;
        while (n > 0) {
            int remainder = n % 2;
            if (remainder == 1) {
                current_ones++;
                max_ones = Math.max(max_ones, current_ones);
            } else {
                current_ones = 0;
            }
            n = n >> 1;
        }
        System.out.println(max_ones);
        scanner.close();
    }
}
