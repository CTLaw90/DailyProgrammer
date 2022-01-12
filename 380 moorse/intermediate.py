#daily programmer
#intermediate

import time

starttime = time.time()

moorse_letters = ('.- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --..').split(' ')
words = open('enable1.txt', 'r')
words = words.read()
words = words.split('\n')

words2 = open('words2.txt', 'w')

def smoosh(x):
	result  = []
	for i in x:
		result.append(str(moorse_letters[ord(i.lower()) - 97]))	
	result = (''.join(result))
	return(result)
	
def rev_smoosh(curword, remaining):
	checkword = []
	for i in range(1,5):
		checkword = remaining[:i]
		if (checkword in moorse_letters) and( chr(moorse_letters.index(checkword) + 97) not in curword):
			if (len(remaining) - i == 0):
				print((str(curword + chr(moorse_letters.index(checkword) + 97)) + '\n'))
				print(time.time() - starttime)	
				exit()
			else:
				rev_smoosh(curword + chr(moorse_letters.index(checkword) + 97), remaining[i:])
	return(True)
		
rev_smoosh('', '......-..--...---.-....---...--....--.-..---.....---.-.---..---.-....--.-.---.-.--')

print(starttime - time.time())		
		