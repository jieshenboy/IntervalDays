# -*- coding: UTF-8 –*-


def YearDays(year):
    LeapYear = 366
    CommYear = 365
    LeapFebruary = 28
    CommFebruary = 29
    if(year%100==0 | year%4==0):
        print("This is LeapYear")
        YearDays = 366
        FebruaryDays  = 29
        return YearDays,FebruaryDays
    else:
        YearDays = 365
        FebruaryDays = 28
        return YearDays, FebruaryDays
def InterYearDays(year1, year2):
    sum = 0
    if(year1 == year2):
        return 0
    if(abs(year1-year2)==1):
        return 0
    for i in range(year1+1, year2):
        day = YearDays(i)[0]
        print(i)
        sum += day

        return sum

def MonDays(year, month):
    if (month == 2):
        MDays = YearDays(year)[1]

    elif(month in [1,3,5,7,8,10,12]):
        MDays = 31

    else:
        MDays = 30

    return MDays
#当年过去的时间
def GoDays(year, month, day):
    sum = 0
    for i in range(0, month):
        sum += MonDays(year,i)
    sum += day
    return sum
#当年还没有过去的时间
def NoDays(year, month, day):
    nodays = YearDays(year)[0] - GoDays(year, month, day)
    return nodays

def FirstDate(year1, month1, day1, year2, month2, day2):
    if(year1==year2):
        if(month1 == month2):
            if(day1 == day2 ):
                return year1,month1,day1
            else:
                if(day1 > day2):
                    return year1, month1, day1
                else:
                    return year2, month2, day2
        else:
            if(month1>month2):
                return year1, month1, day1
            else:
                return year2, month2, day2
    else:
        if(year1>year2):
            return year1, month1, day1
        else:
            return year2, month2, day2

def SecondDate(year1, month1, day1, year2, month2, day2):
    if(year1==year2):
        if(month1 == month2):
            if(day1 == day2 ):
                return year1,month1,day1
            else:
                if(day1 > day2):
                    return year2, month2, day2
                else:
                    return year1, month1, day1
        else:
            if(month1>month2):
                return year2, month2, day2
            else:
                return year1, month1, day1
    else:
        if(year1>year2):
            return year2, month2, day2
        else:
            return year1, month1, day1




def computeDaysBetween(year1, month1, day1, year2, month2, day2):
    firstdate = FirstDate(year1, month1, day1, year2, month2, day2)
    seconddate =  SecondDate(year1, month1, day1, year2, month2, day2)
    #days = firstdate - seconddate
    #=firstdate's godays + seconddate'nodays + InterYearDays(secondyear,firstyear)
    firstyear = firstdate[0]
    firstmonth = firstdate[1]
    firstday = firstdate[2]

    secondyear = seconddate[0]
    secondmonth = seconddate[1]
    secondday = seconddate[2]

    Fgodays = GoDays(firstyear, firstmonth, firstday)
    Snodays = NoDays(secondyear, secondmonth, secondday)
    IYdays = InterYearDays(secondyear,firstyear)
    print(Fgodays+Snodays+IYdays)

    return Fgodays+Snodays+IYdays

if __name__ == '__main__':
    computeDaysBetween(2017,1,31,2018,1,20)