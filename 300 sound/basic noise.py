#Basic noise

import winsound

notes = [262, 294, 330, 349, 392, 440, 494, 523]

'''
for note in notes:
	print note
	winsound.Beep(note, 100)
'''	
	
for i in xrange(50):
	winsound.Beep(262,50)
	winsound.Beep(330,50)
	winsound.Beep(392,50)