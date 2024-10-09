#!/bin/python3

#
# https://www.hackerrank.com/challenges/python-time-delta/problem?isFullScreen=true
#
# INCOMPLETE
#
import math
import os
import random
import re
import sys
import time
from datetime import date
from datetime import datetime



t1 = "Sat 02 May 2015 19:54:36 +0530"
t2 = "Fri 01 May 2015 13:54:36 -0000"


# Complete the time_delta function below.
def time_delta(t1, t2):
    t1_time = get_time_in_seconds(t1)
    print(t1_time)
    t2_time = get_time_in_seconds(t2)
    print(t2_time)
    print(t1_time - t2_time)


def get_time_in_seconds(t1):

    weekday, day, month, year, time0, offset = t1.split(' ')

    # print(weekday, day, month, year, time0, offset)

    hour, minute, second = time0.split(':')

    weekday = convert_weekday(weekday)
    month = convert_month(month)
    dayOfYear = day_of_year(year, str(month), day)
    offset = calcOffset(offset)

    time_tuple = (int(year), month, int(day), int(hour), int(minute), int(second), weekday, dayOfYear, 0)

    print(time_tuple)
    # print(time.mktime(time_tuple))
    # print(offset)

    actual_time = time.mktime(time_tuple) + offset

    # print(actual_time)

    return actual_time



def convert_weekday(weekday):
    dict_day = {
        "Mon": 0,
        "Tue": 1,
        "Wed": 2,
        "Thur": 3,
        "Fri": 4,
        "Sat": 5,
        "Sun": 6
    }

    return dict_day[weekday]

def convert_month(month):
    dict_month = {
        "Jan": 1,
        "Feb": 2,
        "Mar": 3,
        "Apr": 4,
        "May": 5,
        "Jun": 6,
        "Jul": 7,
        "Aug": 8,
        "Sept": 9,
        "Oct": 10,
        "Nov": 11,
        "Dec": 12
    }

    return dict_month[month]

def day_of_year(year, month, day):
    date_format = "%Y-%m-%d"
    date_string = year + "-" + month + "-" + day
    date_object = datetime.strptime(date_string, date_format)
    return date_object.timetuple().tm_yday

def calcOffset(offset):
    minus = offset[0:1]
    hours = offset[1:3]
    mins = offset[3:5]

    hours = int(hours) * 60 * 60
    mins = int(mins) * 60

    # print(minus, hours, mins)

    total = hours + mins
    
    if minus == "-":
        total = 0 - total

    return total
    


time_delta(t1, t2)


# if __name__ == "__main__":
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     t = int(input())

#     for t_itr in range(t):
#         t1 = input()

#         t2 = input()

#         time_delta(t1, t2)

#         fptr.write(delta + '\n')

#     fptr.close()
