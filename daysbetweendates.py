def nextDay(year, month, day):
	if day < days_per_month(year, month):
		return (year, month, day + 1)
	elif month == 12:
		return (year + 1, 1, 1)
	else:
		return (year, month + 1, 1)

def dateIsBefore(year1, month1, day1, year2, month2, day2):
 	date1 = (year1, month1, day1)
 	date2 = (year2, month2, day2)
 	if date1 <= date2:
 		return True
 	else:
 		return False

def days_per_month(year, month):
	if month in [1, 3, 5, 7, 8, 10, 12]:
		return 31
	if month in [4, 6, 9, 11]:
		return 30
	else:
		if isLeapYear(year):
			return 29
		else:
			return 28
	
#print days_per_month(2, 3) # testing
# year = int(raw_input(">")) # for testing

def isLeapYear(year):
	if year % 100 == 0:
		if year % 400 == 0:
			return True
		else:
			return False
	elif year % 4 == 0:
		return True
	else:
		return False
	
# isLeapYear(year) # testing


def daysBetweenDates(year1, month1, day1, year2, month2, day2):
	date1 = (year1, month1, day1)
	date2 = (year2, month2, day2)

	assert date1 <= date2

	days = 0
	while date1 < date2:
		days += 1
		date1 = nextDay(*date1)
	return days

# Test routine

def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()
