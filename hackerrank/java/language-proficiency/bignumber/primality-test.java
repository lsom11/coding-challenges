import java.io.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;
import java.math.BigInteger;

public class Solution {

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        String n = scanner.nextLine();
        BigInteger f = new BigInteger(n);
        boolean isPrime = f.isProbablePrime(100);
        System.out.println(isPrime ? "prime" : "not prime");
        scanner.close();
    }
}
