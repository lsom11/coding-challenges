import java.io.*;
import java.util.*;


class Node{
	int data;
	Node next;
	Node(int d){
        data = d;
        next = null; }

}


class Solution


{

    public static Node removeDuplicates(Node head) {
        Node temp = head;
      Set < Integer > s = new HashSet < Integer > ();
      s.add(temp.data);
      Node current = temp.next;
      while (current != null) {
          if (s.contains(current.data)) {
              temp.next = current.next;} else {
              s.add(current.data);
              temp = current;}
          current = current.next;}
      return head; }

    public static  Node insert(Node head, int data)
