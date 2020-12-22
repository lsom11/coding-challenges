class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        counter = 0
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                for k in range(j+1, len(arr)):
                    a_pass = abs(arr[i] - arr[j]) <= a
                    b_pass = abs(arr[j] - arr[k]) <= b
                    c_pass = abs(arr[i] - arr[k]) <= c
                    
                    if a_pass and b_pass and c_pass:
                        counter += 1
        return counter