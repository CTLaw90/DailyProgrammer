#Words with Enemies
#Daily programmer 198 Easy

PointsA = 0
PointsB = 0




cont = True
while cont:
	WordA = raw_input('First word: ')
	WordB = raw_input('Second word: ')

	ArrA = []
	ArrB = []

	ArrA2 = []
	ArrB2 = []

	for letter in WordA:
		ArrA.append(letter)
		ArrA2.append(letter)
		
	for letter in WordB:
		ArrB.append(letter)
		ArrB2.append(letter)
		
	for item in ArrA:
		if item in ArrB:
			ArrA2.remove(item)
			ArrB2.remove(item)
			
	print ArrA2, ArrB2
	if len(ArrA2) > len(ArrB2):
		print "Player A wins!"
		PointsA += len(ArrA2) - len(ArrB2)
	if len(ArrB2) > len(ArrA2):
		print "Player B wins!"
		PointsB += len(ArrB2) - len(ArrA2)
	else:
		print "TIE"
	
	while True:
		contV = raw_input("cont?? (y/n):")
		if contV.lower() == 'y':
			break
		if contV.lower() == 'n':
			cont = False
			break
			
	print "Points - A:", PointsA
	print "Points - B:", PointsB
	