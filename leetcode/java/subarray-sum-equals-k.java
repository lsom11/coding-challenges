import java.util.HashMap;

public class Solution {
  public int subarraySum(int[] nums, int k) {
    HashMap<Integer, Integer> arr_sums = new HashMap();
    arr_sums.put(0, 1);

    int sum = 0;
    int result = 0;

    // add numbers onto ongoing sum
    for (int i = 0; i < nums.length; i++) {
      sum += nums[i];

      // if this exists,
      if (arr_sums.containsKey(sum - k)) {
        result += arr_sums.get(sum - k);
      }

      // go through arr, build hash map
      arr_sums.put(sum, arr_sums.getOrDefault(sum, 0) + 1);
    }

    return result;
  }
}