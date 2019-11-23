import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = scan.nextLine();
        String[] terms = s.trim().split("[ !,?\\._'@]+", 0);

        if (terms.length == 1 && terms[0].equals("")) {
            System.out.println(0);
        } else {

            System.out.println(terms.length);
            for (int i = 0; i < terms.length; i++) {
                System.out.println(terms[i]);
            }
        }
        scan.close();
    }
}
