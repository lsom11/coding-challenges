import java.io.*;
import java.util.*;

public class Solution {

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    int index;

    List<Integer> l = new ArrayList<>();
    for (int i = 0; i < n; i++) {
      int num = sc.nextInt();
      l.add(num);
    }
    int q = sc.nextInt();
    for (int i = 0; i < q; i++) {
      sc.nextLine();
      String command = sc.nextLine();
      switch (command) {
      case "Insert":
        index = sc.nextInt();
        int val = sc.nextInt();
        l.add(index, val);
        break;
      case "Delete":
        index = sc.nextInt();
        l.remove(index);
        break;
      default:
        break;
      }
    }
    for (int i : l) {
      System.out.print(i + " ");
    }

  }
}
