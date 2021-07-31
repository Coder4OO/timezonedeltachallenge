#Time zone challenge by Coder400
#Task: Calculate time difference between two dates and timezones.
#Time library is banned in this challenge >:)
import json

class Date():
    def __init__(self, second, minute, hour, day, month, year, timezone):
        self.second = second
        self.minute = minute
        self.hour = hour
        self.day = day
        self.month = month
        self.year = year
        self.timezone = timezone
        self.month_days = {"jan":31, "feb":28.25, "mar":31, "apr":30, "may":31, "jun":30, "jul":31, "aug":31, "sep":30, "oct":31, "nov":30, "dec":31}
    
    def __get_month_seconds__(self):
        keys = list(self.month_days.keys())
        key = keys[self.month-1]
        val = self.month_days[key]
        return val*3600*24


    def __get_year_seconds__(self):
        days = 0
        keys = list(self.month_days.keys())
        for x in range(len(keys)):
            key = keys[x]
            days += self.month_days[key]
        return days*3600*24            

    def return_seconds(self):
        min_s = self.minute*60
        hr_s = self.hour*3600
        day_s = self.day*3600*24
        month_s = self.__get_month_seconds__()
        year_s = self.__get_year_seconds__()
        return self.second+min_s+hr_s+day_s+month_s+year_s

    def delta_time(self, date):
        return abs(self.return_seconds()+self.timezone.offset - date.return_seconds()+date.timezone.offset)


