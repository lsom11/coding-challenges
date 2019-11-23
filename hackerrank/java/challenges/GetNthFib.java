import java.util.*; 

class GetNthFib {
  private static Map<Integer,Integer> memo = new HashMap<>();
  public static int getNthFib(int n) {
		 if (n == 0 || n == 1) {
        return n;
		 }
		
		if (memo.containsKey(n)) {
			return memo.get(n);
		}
		
		int result = getNthFib(n - 1) + getNthFib(n - 2);
		
		memo.put(n, result);
	
		return result;
	}
}
