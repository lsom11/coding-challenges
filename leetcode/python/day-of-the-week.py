import datetime
import calendar

class Solution(object):
    def dayOfTheWeek(self, day, month, year):
        my_date = datetime.datetime(year, month, day)
        print(my_date)
        return calendar.day_name[my_date.weekday()] 
        