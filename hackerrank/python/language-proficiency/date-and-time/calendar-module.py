import datetime
import calendar

month, day, year = map(int, input().split())
my_date = datetime.date(year, month, day)
print(calendar.day_name[my_date.weekday()].upper())
