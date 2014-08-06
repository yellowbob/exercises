#work in progress for a class

def datIsBefore(year1, month1, day1, year2, month2, day2):
	if year1 < year2:
		return True
	if year1 == year2:
		if month1 < month2:
			return True
		if month1 == month2:
			if day 1 < day2:
				return True

	return False


def days_per_month(month1, month2):
	days_in_month = [31, 28, 31, 30, 31 ,30, 31, 31, 30, 31, 30, 31]
	month1 = days_in_month[month1 - 1]
	month2 = days_in_month[month2 - 1]
	return month1, month2
	

print days_per_month(2, 3)

def isLeapYear1(year1):
	if year1 % 4 == 0:
		return "Is leap year"
	elif year1 % 100 == 0 and year1 % 400 == 0:
		return "Is leap year"
	else:
		return "Not a leap year"
		
def isLeapYear(year2):
	if year2 % 4 == 0:
		return "Is leap year"
	elif year2 % 100 == 0 and year2 % 400 == 0:
		return "Is leap year"
	else:
		return "Not a leap year"	

def daysbetweendates(year1, month1, day1, year2, month2, day2):

	assert not dateIsBefore(year2, month2, day2, year1, month1, day1)






