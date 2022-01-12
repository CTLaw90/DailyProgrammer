#192 Markov Chain Error Detection

import string

raw_list = open('enable1.txt')
wordlist = raw_list.read()
wordlist = wordlist.split('\n')

alpha_array = [] * 26
for x in xrange(26):
	alpha_array.append([0] * 26)
	
for x in wordlist:
	counter = 0
	for y in x:
		if counter > 0:
			alpha_array[int(string.lowercase.index(last_y))][int(string.lowercase.index(y))] += 1
		
		counter = counter + 1
		last_y = y

input = "example"

print input

counter = 0
for i in input:
	if counter > 0:
		if alpha_array[int(string.lowercase.index(last_i))][int(string.lowercase.index(i))] == 0:
			print 'Spelling Error!'
	
	counter = counter + 1
	last_i = i
		
# print '[a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z]'	
# for line in alpha_array:
	# print line