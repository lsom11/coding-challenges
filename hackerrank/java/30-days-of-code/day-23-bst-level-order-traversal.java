import java.io.*;
import java.util.*;
class Node{
    Node left,right;
    int data;
    Node(int data){
        this.data=data;
        left=right=null;
    }
}
class Solution{

	static void levelOrder(Node root){
        Queue<Node> q = new LinkedList<>(); 
        Queue<Integer> data = new LinkedList<>();
        Node temp = root;

        q.add(temp); 

        while (!q.isEmpty()) {
            temp = q.remove();
            data.add(temp.data);
            if (temp.left != null) {
                q.add(temp.left);
            } 
            if (temp.right != null) {
                q.add(temp.right);
            }
        }
        for (int num : data) {
            System.out.print(num + " ");
        }
      
    }

	public static Node insert(Node root,int data){