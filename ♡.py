import time
import os

#DATE format:        XX.XX.XXXX
#TIME format:        XX:XX:XX

startingpointdate = '24.11.2024'
startingpointtime = '14:30:00'

months = {
    1: 31,
    2: 28, #29
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

if len(startingpointdate) == 10:
    spday = startingpointdate[0:2]
    spmonth = startingpointdate[3:5]
    spyear = startingpointdate[6:10]
else:
    print('Wrong format for StartingPointDate')
    time.sleep(120)
    exit()
if len(startingpointtime) == 8:
    sphour = startingpointtime[0:2]
    spminute = startingpointtime[3:5]
    spsecond = startingpointtime[6:8]
else:
    print('Wrong format for StartingPointTime')
    time.sleep(120)
    exit()



while True:

    time1 = time.perf_counter_ns()

    daynow = time.strftime('%d')
    monthnow = time.strftime('%m')
    yearnow = time.strftime('%Y')

    hournow = time.strftime('%H')
    minutenow = time.strftime('%M')
    secondnow = time.strftime('%S')



    datenow = daynow+'.'+monthnow+'.'+yearnow
    timenow = hournow+':'+minutenow+':'+secondnow



    twsecond = 0
    twminute = 0
    twhour = 0

    twday = 0
    twmonth = 0
    twyear = 0



    twsecond = int(secondnow) - int(spsecond) + int(twsecond)
    if twsecond < 0:
        twsecond = 60 + int(twsecond)
        twminute = -1
        twsecond = str(twsecond)
    if len(str(twsecond)) != 2:
        twsecond = '0'+str(twsecond)
    else:
        twsecond = str(twsecond)

    twminute = int(minutenow) - int(spminute) + int(twminute)
    if twminute < 0:
        twminute = 60 + int(twminute)
        twhour = -1
        twminute = str(twminute)
    if len(str(twminute)) == 1:
        twminute = '0'+str(twminute)
    else:
        twminute = str(twminute)

    twhour = int(hournow) - int(sphour) + int(twhour)
    if twhour < 0:
        twhour = 24 + int(twhour)
        twday = -1
        twhour = str(twhour)
    if len(str(twhour)) == 1:
        twhour = '0'+str(twhour)
    else:
        twhour = str(twhour)

    twday = int(daynow) - int(spday) + int(twday)
    if twday < 0:
        twday = months[int(monthnow)] + int(twday)
        twmonth = -1
        twday = str(twday)
    if len(str(twday)) == 1:
        twday = '0'+str(twday)
    else:
        twday = str(twday)

    twmonth = int(monthnow) - int(spmonth) + int(twmonth)
    if twmonth < 0:
        twmonth = 12 + int(twmonth)
        twyear = -1
        twmonth = str(twmonth)
    if len(str(twmonth)) == 1:
        twmonth = '0'+str(twmonth)
    else:
        twmonth = str(twmonth)
    
    twyear = int(yearnow) - int(spyear) + int(twyear)
    if twyear < 0:
        twyear = 0 
        twyear = str(twyear)
    if len(str(twyear)) == 1:
        twyear = '000'+str(twyear)
    if len(str(twyear)) == 2:
        twyear = '00'+str(twyear)
    if len(str(twyear)) == 3:
        twyear = '0'+str(twyear)
    else:
        twyear = str(twyear)
    


    timewasteddate = twday+'.'+twmonth+'.'+twyear
    timewastedtime = twhour+':'+twminute+':'+twsecond



    totaltwdays = float(twyear) * 12
    totaltwdays = totaltwdays * 30.4375
    totaltwdays = float(twmonth) * 30.4375 + totaltwdays
    totaltwdays = totaltwdays + float(twday)
    totaltwdays = float(twhour) / 24 + totaltwdays
    totaltwdays = float(twminute) / 60 / 24 + totaltwdays
    totaltwdays = float(twsecond) / 60 / 60 / 24 + totaltwdays
    totaltwdays = round(totaltwdays, 5)
    totaltwdays = str(totaltwdays)

    totaltwmonths = float(totaltwdays) / 30.4375
    totaltwmonths = round(totaltwmonths, 7)
    totaltwmonths = str(totaltwmonths)

    totaltwyears = float(totaltwmonths) / 12
    totaltwyears = round(totaltwyears, 8)
    totaltwyears = str(totaltwyears)

    totaltwhours = float(totaltwdays) * 24
    totaltwhours = round(totaltwhours, 4)
    totaltwhours = str(totaltwhours)

    totaltwminutes = float(totaltwdays) * 24 * 60
    totaltwminutes = round(totaltwminutes, 3)
    totaltwminutes = str(totaltwminutes)

    totaltwseconds = float(totaltwdays) * 24 * 60 * 60
    totaltwseconds = round(totaltwseconds, 0) 
    totaltwseconds = str(totaltwseconds)




    #dates length are 10 symbols
    #times length are 8 symbols

    zeroline =       'ღ ღ ღ ღ ღ ღ ღ ღ ღ ღ ღ ღ ღ ღ ღ ღ ღ ღ ღ ღ ღ ღ ღ ღ ღ ღ   Прошло времени:'+'\n'
    firstline =      'ღ Начало наших отношений (дата)     = '+startingpointdate+     '  ღ   '+'\n'
    secondline =     'ღ Начало наших отношений (время)    = '+startingpointtime+'  '+'  ღ   '+'Года    = '+totaltwyears+'\n'
    thirdline =      'ღ ღ ღ ღ ღ ღ ღ ღ ღ ღ ღ ღ ღ ღ ღ ღ ღ ღ ღ ღ ღ ღ ღ ღ '+       'ღ ღ   '+'Месяца  = '+totaltwmonths+'\n'
    fourthline =     'ღ Прошло времени (дата)             = '+timewasteddate+        '  ღ   '+'Дни     = '+totaltwdays+'\n'
    fifthline =      'ღ Прошло времени (время)            = '+timewastedtime+   '  '+'  ღ   '+'Часы    = '+totaltwhours+'\n'
    sixthline =      'ღ ღ ღ ღ ღ ღ ღ ღ ღ ღ ღ ღ ღ ღ ღ ღ ღ ღ ღ ღ ღ ღ ღ ღ '+       'ღ ღ   '+'Минуты  = '+totaltwminutes+'\n'
    seventhline =    'ღ Время сейчас (дата)               = '+datenow+               '  ღ   '+'Секунды = '+totaltwseconds+'\n'
    eighthline =     'ღ Время сейчас (время)              = '+timenow+          '  '+'  ღ   '+'\n'
    ninethline =     'ღ ღ ღ ღ ღ ღ ღ ღ ღ ღ ღ ღ ღ ღ ღ ღ ღ ღ ღ ღ ღ ღ ღ ღ ღ ღ   Люблю тебя, Нозия ^^'+'\n'
    

    allinfomessage = zeroline+firstline+secondline+thirdline+fourthline+fifthline+sixthline+seventhline+eighthline+ninethline

 
    time2 = time.perf_counter_ns() - time1
    time2 = time2 / 1000000000
    time3 = 1.0 - time2
    if time3 < 0:
        time3 = 0
    #задержка в миллисекундах. сколько миллисекунд требуется для осуществления всех строчек кода в этом бесконечном цикле

    os.system('cls')

    print(allinfomessage)

    time.sleep(time3)