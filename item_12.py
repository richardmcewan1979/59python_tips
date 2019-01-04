#Avoid else blocks after for and while loops
#else useful when searching for somethign like this coprime example

a = 4
b = 9
for i in range(2, min(a, b)+1):
	print('Testing', i)
	if a % i == 0 and b % i ==0:
		print('not coprime')#This condition never met
		break
else:
	print('coprime')
#coprime means greatest common divisor is 1

#in practice we would write a helper function in two common styles.
#These are much easier to read and understand.

def coprime(a,b):
	for i in range(2,min(a, b) +1):
		if a % i == 0 and b % i == 0:
			return False
	return True

#alternatively

def coprime2(a,b):
	is_coprime = True
	for i in range(2, min(a, b) + 1):
		if a % i ==0 and b % i == 0:
			is_coprime = False
			break
	return is_coprime

print(coprime(4,9))
print(coprime(3,9))

print(coprime2(4,9))
print(coprime2(3,9))