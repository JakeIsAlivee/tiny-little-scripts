import datetime
import time

import os

Months_leapyear = {
    1: 31,
    2: 29,
    3: 31, 
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
} 
Months = {
    1: 31,
    2: 28,
    3: 31, 
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
} 

date1day = int(24)
date1month = int(2)
date1year = int(2025)
date1hour = int(0)
date1minute = int(0)
date1second = int(0)

cycle = True

if len(str(date1day)) == 1:
    str_date1day = str('0'+str(date1day))
else:
    str_date1day = str(str(date1day))
    
if len(str(date1month)) == 1:
    str_date1month = str('0'+str(date1month))
else:
    str_date1month = str(str(date1month))

if len(str(date1year)) == 3:
    str_date1year = str('0'+str(date1year))
if len(str(date1year)) == 2:
    str_date1year = str('00'+str(date1year))
if len(str(date1year)) == 1:
    str_date1year = str('000'+str(date1year))
else:
    str_date1year = str(str(date1year))

if len(str(date1hour)) == 1:
    str_date1hour = str('0'+str(date1hour))
else:
    str_date1hour = str(str(date1hour))

if len(str(date1minute)) == 1:
    str_date1minute = str('0'+str(date1minute))
else:
    str_date1minute = str(str(date1minute))

if len(str(date1second)) == 1:
    str_date1second = str('0'+str(date1second))
else:
    str_date1second = str(str(date1second))



date1datetime_print = str_date1day+'.'+str_date1month+'.'+str_date1year+' '+str_date1hour+':'+str_date1minute+':'+str_date1second

while True:
    
    os.system('cls||clear')
    
    dayNOW = int(time.strftime('%d'))
    monthNOW = int(time.strftime('%m'))
    yearNOW = int(time.strftime('%Y'))

    hourNOW = int(time.strftime('%H'))
    minuteNOW = int(time.strftime('%M'))
    secondNOW = int(time.strftime('%S'))

        
        
    
    str_dayNOW = str(time.strftime('%d'))
    str_monthNOW = str(time.strftime('%m'))
    str_yearNOW = str(time.strftime('%Y'))

    str_hourNOW = str(time.strftime('%H'))
    str_minuteNOW = str(time.strftime('%M'))
    str_secondNOW = str(time.strftime('%S'))

    datetimeNOW_print = str(str_dayNOW+'.'+str_monthNOW+'.'+str_yearNOW+' '+str_hourNOW+':'+str_minuteNOW+':'+str_secondNOW)

    years_leftto_date1 = date1year - yearNOW
    months_leftto_date1 = date1month - monthNOW
    days_leftto_date1 = date1day - dayNOW
                 
    hours_leftto_date1 = date1hour - hourNOW
    minutes_leftto_date1 = date1minute - minuteNOW
    seconds_leftto_date1 = date1second - secondNOW
    
    

    if hours_leftto_date1 < 0:
        hours_leftto_date1 = 23 + date1hour - hourNOW
        days_leftto_date1 -= 1
    
    if minutes_leftto_date1 < 0:
        minutes_leftto_date1 = 60 + date1minute - minuteNOW 
        hours_leftto_date1 -= 1
    
    if seconds_leftto_date1 < 0:
        seconds_leftto_date1 = 60 + date1second - secondNOW
        minutes_leftto_date1 -= 1
    
    
    
    if days_leftto_date1 < 0:
        if yearNOW / 4:
            days_leftto_date1 = Months_leapyear[monthNOW] + date1day - dayNOW
            months_leftto_date1 -=1
            
        else:
            days_leftto_date1 = Months[monthNOW] + date1day - dayNOW
            months_leftto_date1 -=1
            
    if hours_leftto_date1 < 0:
        hours_leftto_date1 = 23 + date1hour - hourNOW
        days_leftto_date1 -=1
    
    if minutes_leftto_date1 < 0:
        minutes_leftto_date1 = 60 + date1minute - minuteNOW 
        hours_leftto_date1 -= 1
    
    if seconds_leftto_date1 < 0:
        seconds_leftto_date1 = 60 + date1second - secondNOW
        minutes_leftto_date1-=1
    
    
    
    if days_leftto_date1 < 0:
        if yearNOW / 4:
            days_leftto_date1 = Months_leapyear[monthNOW] + date1day - dayNOW
            months_leftto_date1 -=1
            
        else:
            days_leftto_date1 = Months[monthNOW] + date1day - dayNOW
            months_leftto_date1 -=1
 
    if months_leftto_date1 < 0:
        months_leftto_date1 = 12 + date1month - monthNOW
        years_leftto_date1 -= 1
 
 
    
    if len(str(days_leftto_date1)) == 1:
        str_days_leftto_date1 = str('0'+str(days_leftto_date1))
    else:
        str_days_leftto_date1 = str(days_leftto_date1)
    
    if len(str(months_leftto_date1)) == 1:
        str_months_leftto_date1 = str('0'+str(months_leftto_date1))
    else:
        str_months_leftto_date1 = str(str(months_leftto_date1))

    if len(str(years_leftto_date1)) == 3:
        str_years_leftto_date1 = str('0'+str(years_leftto_date1))
    if len(str(years_leftto_date1)) == 2:
        str_years_leftto_date1 = str('00'+str(years_leftto_date1))
    if len(str(years_leftto_date1)) == 1:
        str_years_leftto_date1 = str('000'+str(years_leftto_date1))
    else:
        str_years_leftto_date1 = str(str(years_leftto_date1))
    


    if len(str(hours_leftto_date1)) == 1:
        str_hours_leftto_date1 = str('0'+str(hours_leftto_date1))
    else:
        str_hours_leftto_date1 = str(str(hours_leftto_date1))

    if len(str(minutes_leftto_date1)) == 1:
        str_minutes_leftto_date1 = str('0'+str(minutes_leftto_date1))
    else:
        str_minutes_leftto_date1 = str(str(minutes_leftto_date1))

    if len(str(seconds_leftto_date1)) == 1:
        str_seconds_leftto_date1 = str('0'+str(seconds_leftto_date1))
    else:
        str_seconds_leftto_date1 = str(str(seconds_leftto_date1))


    if years_leftto_date1 < 0 or months_leftto_date1 < 0 or days_leftto_date1 < 0:
        years_leftto_date1 = 0
        months_leftto_date1 = 0
        days_leftto_date1 = 0
            
        hours_leftto_date1 = 0
        minutes_leftto_date1 = 0
        seconds_leftto_date1 = 0
        
        totalyears_left = 0
        totalmonths_left = 0
        totaldays_left = 0

        totalhours_left = 0
        totalminutes_left = 0
        totalseconds_left = 0

        date_leftto_date1_print = str('00.00.0000')

        time_leftto_date1_print = str('00:00:00')



        print("Time's up!\n")

        print('Date today:            |    Total years left = '+str(totalyears_left))
        print(datetimeNOW_print+'    |    Total months left = '+str(totalmonths_left))

        print('Counting to:           |    Total days left = '+str(totaldays_left))
        print(date1datetime_print+'    |    Total hours left = '+str(totalhours_left))

        print('Time left:             |    Total minutes left = '+str(totalminutes_left))
        print(date_leftto_date1_print+' '+time_leftto_date1_print+'    |    Total seconds left = '+str(totalseconds_left))

        time.sleep(300)
        continue
    

    date_leftto_date1_print = str(str_days_leftto_date1 + '.'+str_months_leftto_date1+'.'+str_years_leftto_date1)

    time_leftto_date1_print = str(str_hours_leftto_date1+':'+str_minutes_leftto_date1+':'+str_seconds_leftto_date1)
    


    totalyears_left = years_leftto_date1
    
    totalmonths_left = totalyears_left * 12 + months_leftto_date1
    
    numofdays_todaysmonth = 0

    if yearNOW / 4:
        
        totaldays_left = 0
        monthfor_numofdays = monthNOW
        year_calibration = date1year - yearNOW


        while cycle == True:
            if year_calibration == 0:
                if monthfor_numofdays > date1month - 1:
                    break
            
            if year_calibration > 0:
                
                if monthfor_numofdays > 12:
                    monthfor_numofdays = 1
                    year_calibration -= 1

           
            numofdays_todaysmonth = Months_leapyear[monthfor_numofdays]
            totaldays_left += numofdays_todaysmonth
            monthfor_numofdays += 1
            
        totaldays_left += days_leftto_date1     
    
    
    
    else:
        totaldays_left = 0
        monthfor_numofdays = monthNOW
        year_calibration = date1year - yearNOW

        while cycle == True:
            if year_calibration == 0:
                if monthfor_numofdays > date1month - 1:
                    break
            
            if year_calibration > 0:
                
                if monthfor_numofdays > 12:
                    monthfor_numofdays = 1
                    year_calibration -= 1
                    
            
            numofdays_todaysmonth = Months[monthfor_numofdays]
            totaldays_left += numofdays_todaysmonth
            monthfor_numofdays += 1
            
        totaldays_left += days_leftto_date1     
      
    
    
    
    
    totalhours_left = totaldays_left * 24 + hours_leftto_date1
    totalminutes_left = totalhours_left * 60 + minutes_leftto_date1
    totalseconds_left = totalminutes_left * 60 + seconds_leftto_date1

    if totalyears_left > 999:
        print('Are you insane?\n')

    print('Date today:            |    Total years left = '+str(totalyears_left))
    print(datetimeNOW_print+'    |    Total months left = '+str(totalmonths_left))

    print('Counting to:           |    Total days left = '+str(totaldays_left))
    print(date1datetime_print+'    |    Total hours left = '+str(totalhours_left))

    print('Time left:             |    Total minutes left = '+str(totalminutes_left))
    print(date_leftto_date1_print+' '+time_leftto_date1_print+'    |    Total seconds left = '+str(totalseconds_left))


    
    time.sleep(0.9)