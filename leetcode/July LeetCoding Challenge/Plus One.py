class Solution:
    def plusOne(self, digits):
        digits = [0] + digits
        
        end = len(digits) - 1
        while digits[end] == 9:
            end -= 1
    
        digits[end] += 1
        digits[end+1:] = [0] * (len(digits)-1-end)
                   
        return digits if digits[0] != 0 else digits[1:] 