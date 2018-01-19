# -*- coding: UTF-8 –*-

#设定年份的天数模块
def YearDays(year):
    if(year%100!=0 and year%4==0):
        YearDays = 366
        FebruaryDays  = 29
        return YearDays,FebruaryDays
    else:
        YearDays = 365
        FebruaryDays = 28
        return YearDays, FebruaryDays
#设定两年间相差的天数模块
def InterYearDays(year1, year2):
    sum = 0
    if(year1 == year2):
        return 0
    if(abs(year1-year2)==1):
        return 0
    for i in range(year1+1, year2):
        day = YearDays(i)[0]
        sum += day


    return sum

#设定月份天数的模块
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
#排序靠后的时间
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
#排序靠前的时间
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



#程序主逻辑模块
def computeDaysBetween(year1, month1, day1, year2, month2, day2):
    try:
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
        Sgodays = GoDays(secondyear,secondmonth,secondday)
    #    Fnodays = NoDays(firstyear, firstmonth, firstday)
        Snodays = NoDays(secondyear, secondmonth, secondday)

        #IntervalDays
        if (firstyear==secondyear):
            IntervalDays = abs(Fgodays-Sgodays)
            print(IntervalDays)
            return IntervalDays

        else:
            IYdays = InterYearDays(secondyear,firstyear)
            IntervalDays = Fgodays+Snodays+IYdays
            print(IntervalDays)

            return IntervalDays
    except:
        print("执行异常：\n检查是否参数传入正确\n正确例如：(2017,1,31,2018,1,29)")






if __name__ == '__main__':
    #执行computeDaysBetween函数来调用主函数：
    #执行格式为：
    #computeDaysBetween(year1,month1,day1,year2,month2,day2)
    computeDaysBetween(2016,1,31,2018,1,20)
    computeDaysBetween(2008,7,18,2025,2,1)