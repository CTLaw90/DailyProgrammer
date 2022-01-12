#DAILYPROGRAMER CHALLENGE 338 EASY
#WHAT DAY IS IT

day_name = {	0: 'MONDAY',
				1: 'TUESDAY',
				2: 'WEDNESDAY',
				3: 'THURSDAY',
				4: 'FIRDAY',
				5: 'SATURDAY',
				6: 'SUNDAY'	}
				
month_days = { 	0: 31,
				1: 28,
				2: 31,
				3: 30,
				4: 31,
				5: 30,
				6: 31,
				7: 31,
				8: 30,
				9: 31,
				10: 30,
				11: 31	}
		
input_date = '2017 10 30'	#yyyy mm dd

year,month,date = input_date.split(' ')
year,month,date = int(year), int(month), int(date)

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
	leap = True
else:
	leap = False

total_days = 0	#1 1 1 was a saturday using US calendar
for i in xrange(1,year):	
	if (i % 4 == 0 and i % 100 != 0) or (i % 400 == 0):
		total_days += 366
	else:
		total_days += 365

for j in xrange(month-1):
	if (j == 1) and leap:
		total_days += 1
	total_days += month_days[j]
	
total_days += date-1


print input_date, "WAS A", day_name[total_days%7]