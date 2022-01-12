#dailyprogrammer 196
#rail fence cypher


def rail(input_text):
	mode = input_text[0:3]
	if mode != "enc" and mode != "dec":
		print mode
		print "Must choose enc or dec for mode!"
		return
	
	n = int(input_text[4])
	
	input_text = input_text[6:]
	
	if mode == "enc":
		return enc(n, input_text)
		
	else:
		return dec(n, input_text)


def enc(n, input_text):
	layers = {}

	i = 0
	while input_text != "":
		j = i % (n + (n - 1) - 1)
		if j > (n-1) and j < (2*n - 1):
			j = (n - 1) - (j - (n - 1))
		if j in layers.keys():
			layers[j] = layers[j] + input_text[0]
		else:
			layers[j] = input_text[0]
		input_text = input_text[1:]
		i += 1
		
	full_text =[]
	for l in layers.keys():
		full_text.append(layers[l])


	return ''.join(full_text)

def dec(n, text):
	j = (n + (n - 1) - 1)
	layers = {}
	y = 0
	for x in range(0, j):
		new_text = []
		i = x
		a = x
		while i < len(text):
			new_text.append(text[y])
			i += j
			y += 1
		# if x > (n-1):
			# a = (n - 1) - (x - (n - 1))
		if a in layers.keys():
			layers[a] = layers[a] + ''.join(new_text)
		elif len(new_text) > 0:
			layers[a] = ''.join(new_text)
	
	
	for x in layers.keys():
		if x != 0 and x != n:
			if x % 2 == 0:
				layers[x-1] = layers[x-1] + layers[x]
				del layers[x]
	
	dec_text = []
		
	
	# ret_text = []
	for x in layers.keys():
		print x, layers[x]

	# return ''.join(ret_text)

print "example format:\nenc 3 helloworld"
	
input = raw_input('>')
end_string = rail(input)

print end_string