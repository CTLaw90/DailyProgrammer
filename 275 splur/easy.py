#daily programmer
#splurthian chem 1

name = raw_input('Enter Name: ')
abrv = raw_input('Enter Abrv: ')

name = name.lower()
abrv = abrv.lower()

valid = False
for letter in xrange(len(name)):
	if name[letter] == abrv[0]:
		for letter2 in xrange(letter, (len(name))):
			if name[letter2] == abrv[1]:
				valid = True

print valid