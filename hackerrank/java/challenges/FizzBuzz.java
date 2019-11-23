import java.io.*;
import java.util.*;

public class FizzBuzz {

  public static void main(String[] args) {
    int i = 1;
    int UPPER_BOUNDS = 100;
    while (i <= UPPER_BOUNDS) {
      if (i % 3 == 0) {
        if (i % 5 == 0) {
          System.out.println("FizzBuzz");
        } else {
          System.out.println("Fizz");
        }
      } else if (i % 5 == 0) {
        System.out.println("Buzz");
      } else {
        System.out.println(i);
      }

      i++;
    }
  }
}
