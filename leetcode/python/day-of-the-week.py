import datetime
import calendar

class Solution(object):
    def dayOfTheWeek(self, day, month, year):
        my_date = datetime.datetime(year, month, day)
        return calendar.day_name[my_date.weekday()] 
        