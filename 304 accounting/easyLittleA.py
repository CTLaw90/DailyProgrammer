#Challenge 304
#Little Accountant



MONTHS = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']

'''
Journal file in format
ACCOUNT; PERIOD; DEBIT; CREDIT;

Chart file in format
ACCOUNT; LABEL;
'''

journal_file = open('journal.txt')
chart_file = open('chart.txt')

journal = journal_file.read()
journal = journal.split('\n')

for line in xrange(len(journal)):
	journal[line] = journal[line].split(';')
	journal[line].pop(-1)

chart = chart_file.read()
chart = chart.split('\n')
chart_key = {}
for line in xrange(len(chart)):
	chart[line] = chart[line].split(';')
	chart[line].pop(-1)
	chart_key[chart[line][0]] = chart[line][1]

'''
Formatting for user_input:
AAAA BBBB CCC-XX DDD-XX EEE
AAAA == STARTING ACCOUNT	[0]
BBBB == ENDING ACCOUNT		[1]
CCC-XX == FIRST PERIOD		[2]
DDD-XX == LAST PERIOD		[3]
EEE == FORMAT				[4]
'''

print 'FORMAT: AAAA BBBB CCC-XX DDD-XX EEE'
print 'ORDER: STARTINGACCOUNT ENDINGACCOUNT FIRSTPEROID ENDPERIOD FORMAT(TEXT OR CSV)'

while True:
	user_input = raw_input('---->')
	
	if user_input == 'END':
		break

	user_input = user_input.split(' ')

	if user_input[0] == '*':
		user_input[0] = '0000'

	if user_input[1] == '*':
		user_input[1] = '9999'

	if user_input[2] == '*':
		user_input[2] = 'JAN-00'

	if user_input[3] == '*':
		user_input[3] = 'DEC-99'
		
	while len(user_input[0]) < 4:
		user_input[0] += '0'
		
	while len(user_input[1]) < 4:
		user_input[1] += '0'	
		


	journal_choice = []

	for item in journal:
		if item[0] >= user_input[0] and item[0] <= user_input[1] and ( MONTHS.index(item[1][0:3]) >= MONTHS.index(user_input[2][0:3]) and MONTHS.index(item[1][0:3]) <= MONTHS.index(user_input[3][0:3]) ):
			journal_choice.append(item)

	totals = ['TOTALS', ' ', 0, 0, 0]
			
	if user_input[4] == 'CSV':
		print '|ACC\t|NAME\t|DEBIT\t|CREDIT\t|BALANCE\t'
		print '------------------------------------------------------------'
		for item in journal_choice:
			print '|'+item[0]+ '\t|'+ chart_key[item[0]]+ '|\t'+ item[2]+ '|\t'+ item[3]+ '|\t'+ str(int(item[2])-int(item[3]))
			totals[2] += int(item[2])
			totals[3] += int(item[3])
			totals[4] += (int(item[2])-int(item[3]))
		print str(totals)
			
	elif user_input[4] == 'TEXT':
		print 'ACC;NAME;DEBIT;CREDIT;BALANCE'
		for item in journal_choice:
			print item[0]+';'+ chart_key[item[0]]+';'+ item[2]+';'+ item[3]+';'+ str(int(item[2])-int(item[3]))+';'
			totals[2] += int(item[2])
			totals[3] += int(item[3])
			totals[4] += (int(item[2])-int(item[3]))
		print totals[0]+';'+' '+';'+str(totals[2])+';'+str(totals[3])+';'+str(totals[4])+';'