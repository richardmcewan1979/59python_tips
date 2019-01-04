from random import randint

random_bits=0
for i in range(4): 
    if randint(0,1):
    	print(i, "hello")
    	random_bits |= 1 << i
    	print(random_bits)

#| = 1 << i part pushes a 0 or 1 onto the binary according to range.