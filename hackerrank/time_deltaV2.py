# Hackerrank Problem
# Python Time Delta
# Author: Andrew Tracey
# Completed: October 11, 2021

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

# Version 2:
# Using strptime method to parse string into a datetime object

import sys
import datetime

# Code to replicate Hackerrank STDIN
sys.stdin = '2\nSun 10 May 2015 13:54:36 -0700\nSun 10 May 2015 ' \
            '13:54:36 -0000\nSat 02 May 2015 19:54:36 +0530\n' \
            'Fri 01 May 2015 13:54:36 -0000'

# Begin solution
raw_input = sys.stdin
lines = raw_input.split('\n')
T = int(lines.pop(0))
fmt = '%a %d %B %Y %X %z'
for i in range(T):
    t1 = datetime.datetime.strptime(lines[i*2], fmt)
    t2 = datetime.datetime.strptime(lines[i*2+1], fmt)
    delta = abs(int((t1 - t2).total_seconds()))
    print(delta)  # 25200, 88200
