
#EventsList = [5][12][31] 
EventsList = []#[[[0 for _ in range(5)]  for _ in range(12)]  for _ in range(31)] 
WeekdayEvents = [ ("Morning", "Nothing"), 
            ("First Period", "Nothing"),
            ("Lunch", "Nothing"),
            ("Second Period", "Nothing"),
            ("After School", "Nothing")]
WeekendEvents = [ ("Morning", "Nothing"), 
            ("Evening", "Nothing")]
SpecialEvents = [ ("All day", "Nothing")]

def FillEventList(years, months, days): 
  global EventsList
  global SpecialEvents 
  EventsList = [[[0 for _ in range(days)]  for _ in range(months)]  for _ in range(years)] 
  
  #FirstDay = weekDay(2015, 1, 1 )[0]-1
  currday = 4
  
  for y in EventsList:
    for m in y:
      for d in range(len(m)):
        m[d] = d+1
        CurrentDay = currday%7
        if ( CurrentDay < 6 and CurrentDay > 0):
          m[d] =  WeekdayEvents
        else:
          m[d] =  WeekendEvents
        currday +=1

def GetEventList(year, month, day):
  global EventsList 
  Events = EventsList[year][month][day]    
  
  return Events

friends = ['john', 'pat', 'gary', 'michael']

FillEventList(1,1,31)
i = 0
j =0
k =0

#print "{iteration} ".format(iteration=EventsList)

for i, name in enumerate(EventsList):
    #EventsList
    print "iteration {iteration} is {name}\n".format(iteration=i, name=EventsList)