class Solution {
    private int sumEvenNumbers(int[] A) {
        int count = 0;
        
        for (int num : A) {
            if (num % 2 == 0) {
                count += num;
            }
        }
        
        return count;
    }
    
    public int[] sumEvenAfterQueries(int[] A, int[][] queries) {
        final int arrayLength = A.length;
        
        int[] sumList = new int[arrayLength];
            
        for (int i = 0; i < arrayLength; i++) {
            int idx = queries[i][1];
            int sum = queries[i][0];
            A[idx] += sum;
            
            sumList[i] = sumEvenNumbers(A);
            
        }
        
        return sumList;
    }
}