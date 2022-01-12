#swag

torn = [n for n in range(1000,10000) if sum(divmod(n,100))**2 == n]

print torn