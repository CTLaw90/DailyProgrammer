#DailyProgrammer Challenge162 Easy
#Novel Compression pt.1 Unpacking the Data


data_set = open('data.txt')
# output_data = open('out_data.txt', 'w')

Numb_of_Words = data_set.readline()

Words = []

for i in xrange(1, int(Numb_of_Words) + 1):
	tempWords = data_set.readline()
	tempWords = tempWords.replace('\n', '')
	Words.append(tempWords)

Remaining_Data = data_set.read()

print Numb_of_Words
print Words
print Remaining_Data

xwords = int(Numb_of_Words)
Rem_Data_List = Remaining_Data.split(' ')

#helper code to determine if a string represents an integer
def Is_Int(x):
	try:
		int(x)
		return True
	except ValueError:
		return False


#Translating the code

result_string = []

for char in Rem_Data_List:
	num = char
	last_char = num[-1]
	
	if Is_Int(last_char) == False:
		num = char[0:-1]
	
	print char, num, last_char
	
	if Is_Int(num):
		if int(num) >= 0 and int(num) <= xwords:
			buffer_string.append(str(Words[int(num)]))
			buffer_string.append(' ')
			continue
			
	elif last_char == 'E':
		break
		
	elif last_char == '^':
		if buffer_string != []:
			buffer_string[0] = str(buffer_string[0][0]).upper() + buffer_string[0].lstrip(buffer_string[0][0])
			continue
			
	elif last_char == '!':
		if buffer_string != []:
			buffer_word = ''.join(buffer_string)
			buffer_word = buffer_word.upper()
			result_string.append(buffer_word)
			buffer_string = []
			continue
			
	elif last_char == 'R':
		result_string.append('\n')
		continue
	
	else:
		if result_string != []:
			if result_string[-1][-1:] == ' ':				#gets rid of space before punc.
				result_string[-1] = result_string[-1][0:-1]
			result_string.append(num)
		
	buffer_word = ''.join(buffer_string)	#clears buffer
	result_string.append(buffer_word)
	buffer_string = []


result_string = ''.join(result_string)
print result_string
# output_data.write(string_loc);

data_set.close()
# output_data.close()
