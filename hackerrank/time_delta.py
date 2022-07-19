# Hackerrank Problem
# Python Time Delta

# Link: https://www.hackerrank.com/challenges/python-time-delta/problem
# --- PROBLEM DESCRIPTION ---
# When users post an update on social media, such as a URL, image,
#  status update etc., other users in their network are able to view this new
#  post on their news feed. Users can also see exactly when the post was
#  published, i.e, how many hours, minutes or seconds ago.

# Since sometimes posts are published and viewed in different time zones,
# this can be confusing. You are given two timestamps of one such post that
# a user can see on his newsfeed in the following format:
#  - Day dd Mon yyyy hh:mm:ss +xxxx
# Here +xxxx represents the time zone. Your task is to print the absolute
# difference (in seconds) between them.

# Input Format:
#  - The first line contains T, the number of testcases.
#  - Each testcase contains 3 lines, representing time t(1) and time t(2).
# Constraints:
#  - Input contains only valid timestamps.
# Output Format:
#  - Print the absolute difference  in seconds.

# Sample Input 0
# 2
# Sun 10 May 2015 13:54:36 -0700
# Sun 10 May 2015 13:54:36 -0000
# Sat 02 May 2015 19:54:36 +0530
# Fri 01 May 2015 13:54:36 -0000

# Sample Output 0
# 25200
# 88200

# Developer Note:
# PLEASE SEE V2 FOR ALTERNATE SOLUTION
# For this solution, I made the mistake of assuming that the input format of
#  the date times was essentially useless, and just unique to this problem.
#  Therefore, I parsed it manually. I later learned that the format can be
#  parsed for the datetime module.
# I also misunderstood from the problem description that the Month input
#  format would be the first 3 letters, when it is in fact the full Month.
# The examples only used May...ugh
# While this solution works in PyCharm, Hackerrank was not recognizing
# datetime.timezone as a method.


# Begin solution
import sys
import datetime


def get_datetime(dt_string):
    # takes dt_string of format "Day dd Mon yyyy hh:mm:ss -0000"
    year = int(dt_string[11:15])
    month_str = dt_string[7:10]
    month = get_month(month_str)
    day = int(dt_string[4:6])
    hour = int(dt_string[16:18])
    minute = int(dt_string[19:21])
    second = int(dt_string[22:24])
    tz_string = dt_string[-5:]
    tz = get_timezone(tz_string)
    date_time = datetime.datetime(year, month, day, hour, minute, second,
                                  tzinfo=tz)
    return date_time


def get_month(month_string):
    # takes month_string of format "Mon" (e.g. "Mar", "Jun", etc.)
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep",
              "Oct", "Nov", "Dec"]
    month_int = months.index(month_string) + 1
    return month_int


def get_timezone(tz_string):
    # takes tz_string of format "-0000"
    tz_hr = int(tz_string[1:3])
    tz_min = int(tz_string[3:])
    time_zone = None
    if tz_string[0] == "-":
        time_zone = datetime.timezone(
            datetime.timedelta(hours=-tz_hr, minutes=-tz_min)
        )
    elif tz_string[0] == "+":
        time_zone = datetime.timezone(
            datetime.timedelta(hours=tz_hr, minutes=tz_min)
        )
    return time_zone


# Code to replicate Hackerrank STDIN
sys.stdin = '2\nSun 10 May 2015 13:54:36 -0700\nSun 10 May 2015 ' \
            '13:54:36 -0000\nSat 02 May 2015 19:54:36 +0530\n' \
            'Fri 01 May 2015 13:54:36 -0000'

raw_input = sys.stdin.split('\n')
T = int(raw_input[0].strip())
testcases = raw_input[1:]
results = []
for x in range(T):
    t1 = get_datetime(testcases[x*2])
    t2 = get_datetime(testcases[x*2 + 1])
    result = t1 - t2
    result_seconds = int(result.total_seconds())
    results.append(result_seconds)

for result in results:
    print(result)  # 25200, 88200
