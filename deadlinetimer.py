import time
import os

#DATE format:        XX.XX.XXXX
#TIME format:        XX:XX:XX

startingpointdate = '01.01.2020'
startingpointtime = '00:00:00'
deadlinedate = '01.01.2030'
deadlinetime = '00:00:00'

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


if len(deadlinedate) == 10:
    dlday = deadlinedate[0:2]
    dlmonth = deadlinedate[3:5]
    dlyear = deadlinedate[6:10]
else:
    print('Wrong format for DeadlineDate')
    time.sleep(120)
    exit()
if len(deadlinetime) == 8:
    dlhour = deadlinetime[0:2]
    dlminute = deadlinetime[3:5]
    dlsecond = deadlinetime[6:8]
else:
    print('Wrong format for DeadlineTime')
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





    tlsecond = 0
    tlminute = 0
    tlhour = 0
    
    tlday = 0
    tlmonth = 0
    tlyear = 0


    tlsecond = int(dlsecond) - int(secondnow) + int(tlsecond)
    if tlsecond < 0:
        tlsecond = 60 + tlsecond
        tlminute = -1
        tlsecond = str(tlsecond)
    if len(str(tlsecond)) == 1:
        tlsecond = '0'+str(tlsecond)
    else:
        tlsecond = str(tlsecond)

    tlminute = int(dlminute) - int(minutenow) + int(tlminute)
    if tlminute < 0:
        tlminute = 60 + tlminute
        tlhour = -1
        tlminute = str(tlminute)
    if len(str(tlminute)) == 1:
        tlminute = '0'+str(tlminute)
    else:
        tlminute = str(tlminute)

    tlhour = int(dlhour) - int(hournow) + int(tlhour)
    if tlhour < 0:
        tlhour = 24 + tlhour
        tlday = -1
        tlhour = str(tlhour)
    if len(str(tlhour)) == 1:
        tlhour = '0'+str(tlhour)
    else:
        tlhour = str(tlhour)

    tlday = int(dlday) - int(daynow) + int(tlday)
    if tlday < 0:
        tlday = months[int(monthnow)] + int(tlday) - 1
        tlmonth = -1
        tlday = str(tlday)
    if len(str(tlday)) == 1:
        tlday = '0'+str(tlday)
    else:
        tlday = str(tlday)

    tlmonth = int(dlmonth) - int(monthnow) + int(tlmonth)
    if tlmonth < 0:
        tlmonth = 12 + int(tlmonth)
        tlyear = -1
        tlmonth = str(tlmonth)
    if len(str(tlmonth)) == 1:
        tlmonth = '0'+str(tlmonth)
    else:
        tlmonth = str(tlmonth)

    tlyear = int(dlyear) - int(yearnow) + int(tlyear)
    if tlyear < 0:
        tlyear = 0
        tlyear = str(tlyear)
    if len(str(tlyear)) == 1:
        tlyear = '000'+str(tlyear)
    if len(str(tlyear)) == 2:
        tlyear = '00'+str(tlyear)
    if len(str(tlyear)) == 3:
        tlyear = '0'+str(tlyear)
    else:
        tlyear = str(tlyear)

    

    timeleftdate = tlday+'.'+tlmonth+'.'+tlyear
    timelefttime = tlhour+':'+tlminute+':'+tlsecond



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


    totaltldays = float(tlyear) * 12
    totaltldays = totaltldays * 30.4375
    totaltldays = float(tlmonth) * 30.4375 + totaltldays
    totaltldays = totaltldays + float(tlday)
    totaltldays = float(tlhour) / 24 + totaltldays
    totaltldays = float(tlminute) / 60 / 24 + totaltldays
    totaltldays = float(tlsecond) / 60 / 60 / 24 + totaltldays
    totaltldays = round(totaltldays, 5)
    totaltldays = str(totaltldays)

    totaltlmonths = float(totaltldays) / 30.4375
    totaltlmonths = round(totaltlmonths, 7)
    totaltlmonths = str(totaltlmonths)

    totaltlyears = float(totaltlmonths) / 12
    totaltlyears = round(totaltlyears, 8)
    totaltlyears = str(totaltlyears)

    totaltlhours = float(totaltldays) * 24
    totaltlhours = round(totaltlhours, 4)
    totaltlhours = str(totaltlhours)

    totaltlminutes = float(totaltldays) * 24 * 60
    totaltlminutes = round(totaltlminutes, 3)
    totaltlminutes = str(totaltlminutes)

    totaltlseconds = float(totaltldays) * 24 * 60 * 60
    totaltlseconds = round(totaltlseconds, 0) 
    totaltlseconds = str(totaltlseconds)




    #dates length are 10 symbols
    #times length are 8 symbols

    #all first infos are 34 symbols long

    firstline =      'Starting point (date) = '+startingpointdate+     '  |  '+'Time WASTED:'+'\n'
    secondline =     'Starting point (time) = '+startingpointtime+'  '+'  |  '+'Years = = '+totaltwyears+'\n'
    thirdline =      'Deadline (date) = = = = '+deadlinedate+          '  |  '+'Months  = '+totaltwmonths+'\n'
    fourthline =     'Deadline (time) = = = = '+deadlinetime+     '  '+'  |  '+'Days  = = '+totaltwdays+'\n'
    fifthline =      '                                  '+             '  |  '+'Hours = = '+totaltwhours+'\n'
    sixthline =      'Time wasted (date)  = = '+timewasteddate+        '  |  '+'Minutes = '+totaltwminutes+'\n'
    seventhline =    'Time wasted (time)  = = '+timewastedtime+   '  '+'  |  '+'Seconds = '+totaltwseconds+'\n'
    eighthline =     'Time left (date)  = = = '+timeleftdate+          '  |  '+'Time LEFT:'+'\n'
    ninthline =      'Time left (time)  = = = '+timelefttime+     '  '+'  |  '+'Years = = '+totaltlyears+'\n'
    tenthline =      '                                  '+             '  |  '+'Months  = '+totaltlmonths+'\n'
    eleventhline =   'Time now (date) = = = = '+datenow+               '  |  '+'Days  = = '+totaltldays+'\n'
    twelfthline =    'Time now (time) = = = = '+timenow+          '  '+'  |  '+'Hours = = '+totaltlhours+'\n'
    thirteenthline = '                                  '+             '  |  '+'Minutes = '+totaltlminutes+'\n'
    fourteenthline = '                                  '+             '  |  '+'Seconds = '+totaltlseconds+'\n'
    


    allinfomessage = firstline+secondline+thirdline+fourthline+fifthline+sixthline+seventhline+eighthline+ninthline+tenthline+eleventhline+twelfthline+thirteenthline+fourteenthline


    time2 = time.perf_counter_ns() - time1
    time2 = time2 / 1000000000
    time3 = 1.0 - time2
    if time3 < 0:
        time3 = 0
    #задержка в миллисекундах. сколько миллисекунд требуется для осуществления всех строчек кода в этом бесконечном цикле

    os.system('cls')

    print(allinfomessage)

    time.sleep(time3)