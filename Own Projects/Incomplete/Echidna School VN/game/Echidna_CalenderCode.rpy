#Calender dates and events related code
##############################################################################

init python:
  #------------------------------------------------------
  def SetDate(year, month, day):
    global current_date
    global current_month
    global current_year
    current_date = day
    current_month = month-1
    current_year = year
    ShiftEventsBack(current_year)
    
  #------------------------------------------------------
  def AddMonth(monthsToAdd):
    global current_month
    global current_year
    if ((current_month + monthsToAdd) < 12):
      current_month += 1
    else:
      current_month = 0 + (monthsToAdd-12)
      current_year += 1
      
  #------------------------------------------------------
  def AddDay(daysToAdd):
    global current_date
    if ((current_date + daysToAdd) < MonthsOfTheYear[current_month][2]+1):
      current_date += 1
    else:
      current_date = 1
      AddMonth(1)
      
  #------------------------------------------------------
  
init -1 python :
  def weekDay(year, month, day):
    offset = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
    week   = ['Sunday', 
              'Monday', 
              'Tuesday', 
              'Wednesday', 
              'Thursday',  
              'Friday', 
              'Saturday']
    afterFeb = 1
    if month > 2: afterFeb = 0
    aux = year - 1700 - afterFeb
    # dayOfWeek for 1700/1/1 = 5, Friday
    dayOfWeek  = 5
    # partial sum of days between current date and 1700/1/1
    dayOfWeek += (aux + afterFeb) * 365                  
    # leap year correction    
    dayOfWeek += aux / 4 - aux / 100 + (aux + 100) / 400     
    # sum monthly and day offsets
    dayOfWeek += offset[month - 1] + (day - 1)               
    dayOfWeek %= 7
    return dayOfWeek, week[dayOfWeek]
    
    
##############################################################################
init -1 python :
  global EventsList
  EventsList = []
  WeekdayEvents = [ ("Morning", "Nothing"), 
              ("First Period", "Nothing"),
              ("Lunch", "Nothing"),
              ("Second Period", "Nothing"),
              ("After School", "Nothing")]
  WeekendEvents = [ ("Morning", "Nothing"), 
              ("Evening", "Nothing")]
  SpecialEvents = [ ("All day", "Nothing")]
  
  #------------------------------------------------------
  def FillEventList(): 
    global EventsList 
    #ventsList = [[[SpecialEvents for _ in range(5)]  for _ in range(12)]  for _ in range(31)] 
    
    #FirstDay = weekDay(2015, 1, 1 )[0]-1
    
    EventsList = [0 for _ in range(2000)] 
    #starting from Thur 1st Jan 2015
    StartingDayOffset = weekDay(ArrayStartYear, 1, 1 )[0]
    CurrentDay = 0
    TotalDays = 0
    for d in range(0,2000):
      CurrentDay = (StartingDayOffset+TotalDays)%7
      if ( CurrentDay < 6 and CurrentDay > 0):
        EventsList[d] = WeekdayEvents
      else:
        EventsList[d] = WeekendEvents
      TotalDays += 1
  #------------------------------------------------------
  
  def GetDaysFromStart(year, month, day):
    from datetime import date
    
    #Get the number of days since the Start of the array (01/01/15)
    TimeStartDate = date(ArrayStartYear, 1, 1)
    CurrentDate = date(year, month, day)
    DaysSinceArrayStart = CurrentDate - TimeStartDate
    
    return DaysSinceArrayStart.days 
    
  #------------------------------------------------------
  
  def GetEventList(year, month, day):
    global EventsList
    
    Events = EventsList[GetDaysFromStart(year, month, day)] 
    return Events 
  
  #------------------------------------------------------
  def SetSpecialEvents(year):
    global EventsList
    #National Holidays
    SpecialEvents = [ ("All day", "Nothing")]
    NewYearsDay = [ ("New Years day", "New Years Festival")] 
    Easter = [ ("Easter day", "Egg Hunt")] 
    Halloween = [ ("Halloween day", "Spooky things")] 
    Christmas = [ ("Christmas day", "Christmas Party")] 
    
              
    #Prologue: School Dates / Holidays
    P_FirstDayOfSchool = [ ("Morning", "Tour"), 
              ("Lunch", "Nothing"),
              ("After Lunch", "Inductions")]
              
    P_PracticeTestEvent = [ ("Morning", "Tests"), 
              ("Lunch", "Nothing"),
              ("After Lunch", "Tests")]
              
    P_FundRaiser = [ ("All day", "Fund Raiser")]
    P_PublicHoliday = [ ("Public Holiday", "Day Off")]
              
    P_FinalTestEvent_1 = [ ("Morning", "English Final Test"), 
              ("Lunch", "Nothing"),
              ("After Lunch", "Science Final Test")]
    P_FinalTestEvent_2 = [ ("Morning", "Maths Final Test"), 
              ("Lunch", "Nothing"),
              ("After Lunch", "Nothing")]
              
    P_FinalTestResults = [ ("Morning", "Test Results"), 
              ("Lunch", "Nothing"),
              ("After Lunch", "Goodbyes")]
              
    #School Dates / Holidays
    FirstDayOfSchool = [ ("Morning", "Assembly"), 
              ("Lunch", "Nothing"),
              ("After Lunch", "Inductions")]
                  
              
    HalloweenBreak = [ ("Halloween Break", "Spooky things")] 
    ChristmasBreak = [ ("Christmas Break", "Day Off")]
    MidTermBreak = [ ("Mid Term Break", "Day Off")]
    EasterBreak = [ ("Easter Break", "Day Off")]
    MayDay = [ ("May Day", "Day Off")]
    LastDayOfSchool = [ ("Last day of School", "SchoolParty")]
    SummerHolidays = [ ("Summer Holidays", "Day Off")]
    
    
    EventsList[GetDaysFromStart(year, 1, 1)] = NewYearsDay
    EventsList[GetDaysFromStart(year, 4, 6)] = Easter
    EventsList[GetDaysFromStart(year, 10, 31)] = Halloween
    EventsList[GetDaysFromStart(year, 12, 25)] = Christmas
    
    
    EventsList[GetDaysFromStart(year, 9, 1)] = FirstDayOfSchool
    
    EventsList[GetDaysFromStart(year, 10, 30)] = HalloweenBreak
    #EventsList[GetDaysFromStart(year, 10, 31)] = HalloweenBreak
    
    EventsList[GetDaysFromStart(year, 12, 22)] = ChristmasBreak
    EventsList[GetDaysFromStart(year, 12, 23)] = ChristmasBreak
    EventsList[GetDaysFromStart(year, 12, 24)] = ChristmasBreak
    #EventsList[GetDaysFromStart(year, 12, 25)] = ChristmasBreak
    EventsList[GetDaysFromStart(year, 12, 26)] = ChristmasBreak
    EventsList[GetDaysFromStart(year, 12, 27)] = ChristmasBreak
    EventsList[GetDaysFromStart(year, 12, 28)] = ChristmasBreak
    EventsList[GetDaysFromStart(year, 12, 29)] = ChristmasBreak
    EventsList[GetDaysFromStart(year, 12, 30)] = ChristmasBreak
    EventsList[GetDaysFromStart(year, 12, 31)] = ChristmasBreak    
    
    EventsList[GetDaysFromStart(year, 2, 16)] = MidTermBreak
    EventsList[GetDaysFromStart(year, 2, 17)] = MidTermBreak
    
    EventsList[GetDaysFromStart(year, 4, 2)] = EasterBreak
    EventsList[GetDaysFromStart(year, 4, 3)] = EasterBreak
    EventsList[GetDaysFromStart(year, 4, 4)] = EasterBreak
    EventsList[GetDaysFromStart(year, 4, 5)] = EasterBreak
    EventsList[GetDaysFromStart(year, 4, 6)] = EasterBreak
    EventsList[GetDaysFromStart(year, 4, 7)] = EasterBreak
    EventsList[GetDaysFromStart(year, 4, 8)] = EasterBreak
    EventsList[GetDaysFromStart(year, 4, 9)] = EasterBreak
    EventsList[GetDaysFromStart(year, 4, 10)] = EasterBreak    
    
    EventsList[GetDaysFromStart(year, 5, 4)] = MayDay
    
    EventsList[GetDaysFromStart(year, 6, 30)] = LastDayOfSchool
    
    EventsList[GetDaysFromStart(year, 7, 1)] = SummerHolidays
    
    #---------- Prologue events (June Only)
    
    EventsList[GetDaysFromStart(year, 6, 30)] = LastDayOfSchool
    
    EventsList[GetDaysFromStart(year, 6, 1)] = P_FirstDayOfSchool
    EventsList[GetDaysFromStart(year, 6, 5)] = P_PracticeTestEvent
    EventsList[GetDaysFromStart(year, 6, 12)] = P_FundRaiser
    EventsList[GetDaysFromStart(year, 6, 15)] = P_PublicHoliday
    EventsList[GetDaysFromStart(year, 6, 25)] = P_FinalTestEvent_1
    EventsList[GetDaysFromStart(year, 6, 26)] = P_FinalTestEvent_2
    EventsList[GetDaysFromStart(year, 6, 29)] = P_FinalTestResults
    EventsList[GetDaysFromStart(year, 6, 30)] = LastDayOfSchool
    
    P_FirstDayOfSchool = [ ("Morning", "Tour"), 
              ("Lunch", "Nothing"),
              ("After Lunch", "Inductions")]
              
    P_PracticeTestEvent = [ ("Morning", "Tests"), 
              ("Lunch", "Nothing"),
              ("After Lunch", "Tests")]
              
    P_FundRaiser = [ ("All day", "Fund Raiser")]
    P_PublicHoliday = [ ("Public Holiday", "Day Off")]
              
    P_FinalTestEvent_1 = [ ("Morning", "English Final Test"), 
              ("Lunch", "Nothing"),
              ("After Lunch", "Science Final Test")]
    P_FinalTestEvent_2 = [ ("Morning", "Maths Final Test"), 
              ("Lunch", "Nothing"),
              ("After Lunch", "Nothing")]
              
    P_FinalTestResults = [ ("Morning", "Test Results"), 
              ("Lunch", "Nothing"),
              ("After Lunch", "Goodbyes")]
    
    EventsList[GetDaysFromStart(year, 6, 30)] = LastDayOfSchool
    #----------
    
  #------------------------------------------------------
  def DayHasEvent(year, month, day):
    global EventsList
    
    HasEvent = False
    for d in EventsList[GetDaysFromStart(year, month, day)]:
      if d[1] != "Nothing":
        HasEvent = True
    
    return HasEvent
    
  #------------------------------------------------------
  def IsSchoolDay(year, month, day):
    
    day = weekDay(year, month, day)
    
    if (day[1] == 'Saturday' or day[1] == 'Sunday'):
      return False
      
    return True
    
  def GetSchoolDay(year, month, day):
    
    day = weekDay(year, month, day)
    
    return day[1]
    
  #------------------------------------------------------
  def AddNewEvent(year, month, day, Event):
    global EventsList
    
    EventsList[GetDaysFromStart(year, month, day)] = Event
    
  #------------------------------------------------------
  def ShiftEventsBack(newYear):
    global EventsList
    global ArrayStartYear
    oldYear = ArrayStartYear
  
    if oldYear != newYear:  
      for j in range(1, 500):
        EventsList[j] = EventsList[365+j]
      ArrayStartYear = newYear  
  #------------------------------------------------------
  def DaysUntil(year, month, day):
    from datetime import date
    global current_date
    global current_month
    global current_year
    
    #Get the number of days since the Start of the array (01/01/15)
    CurrentDate = date(current_year, current_month, current_date)
    UntilDate = date(year, month, day)
    TotalDaysUntil = UntilDate - CurrentDate
    
    return TotalDaysUntil.days 
    
  #------------------------------------------------------