
class NodeWithMin {
    public int val;
    public int min;
    public NodeWithMin(int val, int min) {
        this.val = val;
        this.min = min;
    }
}

public class StackMin extends Stack<NodeWithMin> {
    public void push(int val) {
        int newMin = Math.min(value, getMin());
        super.push(new NodeWithMin(value, newMin));
    }

    public int getMin() {
        if (this.isEmpty()) {
            return Integer.MAX_VALUE;
        }

        return peek().min;
    }

    public static void main(String[] args) {
        Stack stack = new Stack();
        stack.push(14);
        System.out.println(stack.getMin()); //min is 14
        stack.push(4);
        System.out.println(stack.getMin()); //min is 4
        stack.push(77);
        System.out.println(stack.getMin()); //min is 4
        stack.push(2);
        System.out.println(stack.getMin()); //min is 2
        stack.pop();
        System.out.println(stack.getMin());//min is 3
        stack.pop();
        System.out.println(stack.getMin());//min is 5
    }
}