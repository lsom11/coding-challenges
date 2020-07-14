class Solution:
    def angleClock(self, hour, minutes):
        H_place = 30*hour + 0.5*minutes
        M_place = 6*minutes
        diff = abs(H_place - M_place)
        return diff if diff <= 180 else 360 - diff