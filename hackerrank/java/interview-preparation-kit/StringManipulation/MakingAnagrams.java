import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class MakingAnagrams {

    static int makeAnagram(String a, String b) {
        Map<Character, Integer> counterA = new HashMap<>();
        Map<Character, Integer> counterB = new HashMap<>();
        int deletionsCount = 0;

        for(int i = 'a'; i <= 'z'; i++) {
            counterA.put((char) i, 0);
            counterB.put((char) i, 0);
        }

        for(char c : a.toCharArray())
            counterA.put(c, counterA.get(c) + 1);
        
        for(char c : b.toCharArray())
            counterB.put(c, counterB.get(c) + 1);

        for (char letter : counterA.keySet()) {
            int countA = counterA.get(letter);
            int countB = counterB.get(letter);

            deletionsCount += Math.abs(countA - countB);
        }


        return deletionsCount;
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        String a = scanner.nextLine();

        String b = scanner.nextLine();

        int res = makeAnagram(a, b);

        bufferedWriter.write(String.valueOf(res));
        bufferedWriter.newLine();

        bufferedWriter.close();

        scanner.close();
    }
}
