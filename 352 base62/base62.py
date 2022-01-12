#Base62 conversion

alpha = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

input = 7026425611433322325
output = []

i = input
while True:
	if i > 62:
		output.append(alpha[i%62])
		i = i/62
	else:
		output.append(alpha[i])
		break
	
output = ''.join(output)

print output[::-1]