class Solution:
    def angleClock(self, hour, minutes):
        if hour == 12:
            hour = 0
        hourD = (hour+minutes/60)*30
        minD = minutes*6
        return min(abs(minD-hourD),360-abs(minD-hourD))