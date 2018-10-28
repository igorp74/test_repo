#test


import calendar

# Go through every month
for month in range(1, 13):
    cal = calendar.monthcalendar(2018, month)
    first_week  = cal[0]
    second_week = cal[1]
    third_week  = cal[2]

    # If a MONDAY presents in the first week, the second MONDAY
    # is in the second week.  Otherwise, the second MONDAY must 
    # be in the third week.
    
    if first_week[calendar.MONDAY]:
        day = first_week[calendar.MONDAY]
        dday = second_week[calendar.MONDAY]
    elif second_week[calendar.MONDAY]:
        day = second_week[calendar.MONDAY]
        dday = third_week[calendar.MONDAY]        
    else:
        day = third_week[calendar.MONDAY]


    print('1st monday in month: %3s: %2s' % (calendar.month_abbr[month], day))
    #print('2nd monday in month: %3s: %2s' % (calendar.month_abbr[month], dday))
    


