#193 Acronym Expander

acronym_list = open('acronyms.txt')
acronyms = acronym_list.read()
acronyms = acronyms.split('\n')
lines = len(acronyms)


abrev = []
full = []

for i in xrange(lines):
	wordsplit = acronyms[i].split(' - ')
	abrev.append(wordsplit[0])
	full.append(wordsplit[1])
	
input = raw_input('type something to deacronymify> ') #input text...

words = input.split(' ') 

x = 0

for j in words:
	if j in abrev:
		words[x] = full[abrev.index(j)]
		
	x = x + 1
		

print ' '.join(words)