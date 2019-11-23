import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        BigInteger a;
        BigInteger b;
        BigInteger sum = BigInteger.valueOf(0);
        BigInteger product = BigInteger.valueOf(0);
        
        a = new BigInteger(sc.nextLine());
        b = new BigInteger(sc.nextLine());
        
        sum = sum.add(a);
        sum = sum.add(b);
        product = a.multiply(b);
        
        System.out.println(sum);
        System.out.println(product);
    }
}

