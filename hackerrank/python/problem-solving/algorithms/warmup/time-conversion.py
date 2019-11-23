#!/bin/python3

import os

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    split = len(s) - 2
    time, time_of_day = s[:split], s[split:]
    print(time, time_of_day)
    if (time_of_day == 'AM'): 
        if s[:2] == "12": 
            return "00" + s[2:-2]
        return time
    else: 
        if s[:2] == "12": 
            return s[:-2] 
        return str(int(time[:2]) + 12) + time[2:] 



if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
