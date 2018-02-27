# -*- coding:UTF-8 -*-
import math as mt

# Algo_1
# There are 4 numbers: 1, 2, 3, 4. How many numbers can be consisted of them without repeated number?
def combine_number():
    n4 = [1, 2, 3, 4]
    for i in range(1, 5):
        for j in range(1, 5):
            for k in range(1, 5):
                for m in n4:
                    if (i == j or i == k or i == m or j == k or j == m or k == m):
                        continue
                    else:
                        res = str(i) + str(j) + str(k) + str(m) + '\n'
                        print(res)
    #print(res)

# Algo_3
# 一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
def total_square_number():
    for m in range(168):
        for n in range(m):
            if m**2 - n**2 == 168:
                x = n**2 - 100
                print(x)

# Algo_4
# 输入某年某月某日，判断这一天是这一年的第几天？
def judge_day_in_year():
    date = input("Pelase input a date(fmt:yyyy-mm-dd): ")
    date_arr = date.split("-")
    year = int(date_arr[0])
    month = int(date_arr[1]) - 1
    day = int(date_arr[2])

    is_leap_year = (year % 100 != 0 and year % 4 == 0) or year % 400 == 0
    days_for_one_year = 0
    if is_leap_year:
        days_for_one_year = 366
    else:
        days_for_one_year = 365

    days_for_month = days_in_month(month, is_leap_year)

    days = 0
    if (month == 0):
        days = day
    else:
        for m in range(0, month - 1):
            days += days_in_month(m, is_leap_year)
        days += day
        
    print(days)


def days_in_month(month, is_leap_year):
    if month == 0:
        return 31
    elif month == 1:
        if is_leap_year:
            return 29
        else:
            return 28
    elif month == 2:
        return 31
    elif month == 3:
        return 30
    elif month == 4:
        return 31
    elif month == 5:
        return 30
    elif month == 6:
        return 31
    elif month == 7:
        return 31
    elif month == 8:
        return 30
    elif month == 9:
        return 31
    elif month == 10:
        return 30
    elif month == 11:
        return 31
    
# Algo_5 输入三个整数 x,y,z，请把这三个数由小到大输出
def output_min_number():
    l = []
    for i in range(3):
        x = int(input('integer:\n'))
        l.append(x)
    l.sort()
    print(l)
    pass

# Algo_6 Fibonacci sequence



output_min_number()            
# judge_day_in_year()
# combine_number()
# total_square_number()