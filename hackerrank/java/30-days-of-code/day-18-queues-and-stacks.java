import java.io.*;
import java.util.*;

public class Solution {
    LinkedList queue;
    LinkedList stack;

    public Solution() {
        queue = new LinkedList();
        stack = new LinkedList();
    }

    public boolean isEmpty() {
        return queue.isEmpty();
    }

    public int peek() {
        return (int) queue.get(0);
    }

    public int size() {
        return queue.size();
    }

    public void pushCharacter(int n) {
        stack.push(n);
    }

    public void enqueueCharacter(int n) {
        queue.addLast(n);
    }

    public int dequeueCharacter() {
        return (int) queue.remove(0);
    }

    public int popCharacter() {
        return (int) stack.pop();
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String input = scan.nextLine();
        scan.close();

        // Convert input String to an array of characters:
        char[] s = input.toCharArray();

        // Create a Solution object:
        Solution p = new Solution();

        // Enqueue/Push all chars to their respective data structures:
        for (char c : s) {
            p.pushCharacter(c);
            p.enqueueCharacter(c);
        }

        // Pop/Dequeue the chars at the head of both data structures and compare them:
        boolean isPalindrome = true;
        for (int i = 0; i < s.length / 2; i++) {
            if (p.popCharacter() != p.dequeueCharacter()) {
                isPalindrome = false;
                break;
            }
        }

        // Finally, print whether string s is palindrome or not.
        System.out.println("The word, " + input + ", is " + ((!isPalindrome) ? "not a palindrome." : "a palindrome."));
    }
}