#daily programmer 380
#easy

moorse_letters = ('.- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --..').split(' ')
words = open('words2.txt', 'r')
words = words.read()
words = words.split('\n')



def smoosh(x):
	result  = []
	for i in x:
		result.append(str(moorse_letters[ord(i.lower()) - 97]))
	
	result = (''.join(result))
	return(result)
	
# for word in words:
	# j = smoosh(word)	
	# print(word, j)
		
		
print(smoosh('abcd'))