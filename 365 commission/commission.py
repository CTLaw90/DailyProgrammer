#daily programmer 365
#commission

data = open('input.txt')
data = data.read()
data = data.split('\n-\n')
sales = data[0]
expenses = data[1]

sales = sales.split('\n')
expenses = expenses.split('\n')

names = sales[1].split('\t')
sales = sales[2].split('\t')
expenses = expenses[2].split('\t')

for i in xrange(len(names)):
	profit = int(sales[i]) - int(expenses[i])
	if profit > 0:
		commission = profit * .062
	else:
		commission = 'EXPENSES EXCEED SALES'
	print 'NAME:\t', names[i], '\tSALES:\t', sales[i], '\tEXPENSES:\t', expenses[i], '\tCOMMISSION:\t', commission