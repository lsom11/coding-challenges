import java.io.*;
import java.util.*;



public class MaximumElement {
    public static void main(String[] args) {
        Stack<Integer> stack = new Stack<>();
        Stack<Integer> maxStack = new Stack<>();

        Scanner sc = new Scanner(System.in);
        int count = sc.nextInt();

        for (int i = 0; i < count; i++) {
            int query = sc.nextInt();

            switch(query) {
                case 1:
                    int val = sc.nextInt();
                    stack.push(val);

                    if (maxStack.isEmpty() || val >= maxStack.peek()) {
                        maxStack.push(val);
                    }

                    break;
                case 2:
                    int data = stack.pop();
                    if (data == maxStack.peek()) {
                        maxStack.pop();
                    }
                    break;
                case 3:
                    System.out.println(maxStack.peek());
                    break;
                default:
                    break;
            }
        }

    }
}

