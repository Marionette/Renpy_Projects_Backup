init python:
  #------------------------------------------------------
  #10 days per week
  #4 weeks per month
  #10 months per year
  #3 seasons per year
  #10 horoscopes per year (random but not repeated)
  List_Horoscopes = [  "Aries",
                       "Aquarius",
                       "Cancer",
                       "Gemini",
                       "Capricorn",
                       "Libra",
                       "Leo",
                       "Virgo",
                       "Scorpio",
                       "Sagittarius" ]
                       
  
  Horoscopes_currentYear = []
  current_Horoscope = 0
  
  current_date = 0
  current_week = 0
  current_month = 0
  current_year = 0
  current_season = 0
    
  SeasonsOfTheYear = [ ("Green Season", "Grn"), 
                    ("Yellow Season", "Yel"), 
                    ("Blue Season", "Blu")]

  DaysOfTheWeek = [ ("1", "Mon"), 
                    ("2", "Tue"), 
                    ("3", "Wed"), 
                    ("4", "Thur"), 
                    ("5", "Fri"), 
                    ("6", "Sat"), 
                    ("7", "Sun"), 
                    ("8", "Fun"), 
                    ("9", "Run"), 
                    ("10", "Lun")]
                    
  MonthsOfTheYear = [ ("Rising Sun", "Jan"),
                      ("Sparkling Springs", "Feb"),
                      ("Green Sprouts", "Mar"),
                      ("Full Blossom", "Apr"),
                      ("???", "May"),
                      ("???", "Jun"),
                      ("Passing Birds", "Jul"),
                      ("Cold Rains ", "Aug"),
                      ("Long Nights", "Sep"),
                      ("Northern Winds ", "Oct")]
                      
                      
                      
  #------------------------------------------------------
  def SetDate(year, month, day):
    global current_date
    global current_month
    global current_year
    current_date = day-1
    current_month = month-1
    current_year = year
    
  #------------------------------------------------------
  def AddMonth(monthsToAdd):
    global current_month
    global current_year
    if ((current_month + monthsToAdd) < 10):
      current_month += 1
    else:
      current_month = 0
      current_year += 1
      
  #------------------------------------------------------
  def AddDay(daysToAdd):
    global current_date
    _days = daysToAdd
    while (_days > 0):
      if ((current_date + 1) <= 40):
        current_date += 1
      else:
        current_date = 1
        AddMonth(1)
      _days -=1
  #------------------------------------------------------
  def AddWeek(weeksToAdd):
    AddDay(weeksToAdd*10)
    
  #------------------------------------------------------
  def GetSeason(currentMonth):
    season = SeasonsOfTheYear[1]
    if (currentMonth < 4):
      season = SeasonsOfTheYear[0]
    if (currentMonth > 6):
      season = SeasonsOfTheYear[2]
    
    return season[0]
  #------------------------------------------------------
  def GetDay(date):
    
    day = date%10
    
    return DaysOfTheWeek[day]
    #return day
  #------------------------------------------------------
  def GetWeek(date):
    
    week = date/10
    
    return week+1    
    
  #------------------------------------------------------
  def RandomiseHoroscopeList():
    global Horoscopes_currentYear
    Horoscopes_currentYear = []
    tempList = list(List_Horoscopes)
    while len(Horoscopes_currentYear) < 9:
        horoscope = renpy.random.choice(tempList)
        Horoscopes_currentYear.append(horoscope)
        tempList.remove(horoscope)
        
  #------------------------------------------------------
    
  def GetHoroscope(month):    
    return List_Horoscopes[month]
    