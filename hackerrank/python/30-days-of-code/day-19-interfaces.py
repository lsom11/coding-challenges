class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        i = 1
        sum = 0
        while i <= n:
            if (n % i == 0):
                sum += i
            i = i + 1
        return sum
