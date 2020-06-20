class Solution:
    def getPermutation(self, n, k):
        numbers = list(range(1,n+1))
        answer = ""
        
        for n_it in range(n,0,-1):
            d = (k-1)//factorial(n_it-1)
            k -= d*factorial(n_it-1)
            answer += str(numbers[d])
            numbers.remove(numbers[d])
                   
        return answer