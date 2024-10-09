# https://www.hackerrank.com/challenges/calendar-module/problem?isFullScreen=true

import calendar


# print(calendar.TextCalendar(firstweekday=6).formatyear(2015))


# mm, dd, yy = list(map(int, input().split()))

day = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]

mm = 10

dd = 1

yy = 2024

print(day[calendar.weekday(yy, mm, dd)])


print(list(calendar.day_name))