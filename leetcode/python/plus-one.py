class Solution(object):
    def plusOne(self, digits):
        n = len(digits)

        for i in reversed(range(n)):
            print(n)
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
            
        new_digits = [1] + digits
        
        return new_digits
