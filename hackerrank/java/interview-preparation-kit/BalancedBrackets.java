import java.util.HashMap;

public class BalancedBrackets {
  private static boolean checkIfBalanced(String str) {
    HashMap<String, String> keys = new HashMap<>();
    keys.put(")", "(");
    keys.put("]", "[");
    keys.put("}", "{");

    Stack stack = new Stack();
    for (char c : str.toCharArray()) {
      String s = Character.toString(c);
      if (keys.containsKey(s)) {
        String item = (String) stack.pop();
        String value = keys.get(s);

        if (!item.equals(value)) {
          return false;
        }

      } else {
        stack.push(s);
      }
    }

    return true;
  }

  public static void main(String[] args) {
    String test1 = "[()]{}{[()()]()}";
    String test2 = "[(])";
    String test3 = "[()]";

    System.out.println(checkIfBalanced(test1)); // true
    System.out.println(checkIfBalanced(test2)); // false
    System.out.println(checkIfBalanced(test3)); // true

  }
}
