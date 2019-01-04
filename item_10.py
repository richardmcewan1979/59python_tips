#item 10: prefer enumerate over range

flavor_list = ['vanilla','chocolate','pecan','strawberry']
for flavor in flavor_list:
	print('%s is delicious' % flavor)

for i in range(len(flavor_list)):
	flavor = flavor_list[i]
	print('%d: %s ' % (i + 1, flavor))

#above harder to read, so use enumerate instead

for i, flavor in enumerate(flavor_list):
	print('%d: %s ' % (i + 1, flavor))

#shorter by using enumerate(list, start)

for i, flavor in enumerate(flavor_list, 1):
	print('%d: %s' % (i, flavor)





