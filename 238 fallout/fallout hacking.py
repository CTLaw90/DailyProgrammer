#daily programmer 238
#fallout hacking game

wordFile = open('enable1.txt')
wordList = wordFile.read()
wordList = wordList.split('\n')
wordBook = {}

for item in wordList:
	if len(item) in wordBook:
		wordBook[len(item)].append(item)
	else:
		wordBook[len(item)] = [item]
	
