import java.io.*;
import java.util.*;

public class StacksAndQueues<D> {
    LinkedList<D> queue;
    LinkedList<D> stack;

    public StacksAndQueues() {
        queue = new LinkedList<>();
        stack = new LinkedList<>();
    }

    public boolean isEmpty() {
        return queue.isEmpty();
    }

    public D peek() {
        return queue.get(0);
    }

    public D size() {
        return queue.size();
    }

    public void pushCharacter(D n) {
        stack.push(n);
    }

    public void enqueueCharacter(D n) {
        queue.addLast(n);
    }

    public D dequeueCharacter() {
        return queue.remove(0);
    }

    public D popCharacter() {
        return stack.pop();
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String input = scan.nextLine();
        scan.close();

        char[] s = input.toCharArray();

        StacksAndQueues p = new StacksAndQueues();

}