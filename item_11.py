#Use zip to process iterators in parallel

names = ['Ceilia', 'Lise', 'Marie']
letters = [len(n) for n in names]
print(letters)

longest_name = None
max_letters = 0

for i in range(len(names)):
	count = letters[i]
	if count > max_letters:
		longest_name = names[i]
		max_letters = count

print(longest_name)

#above hard to read, enumerate better

for i, name in enumerate(names):
	count = letters[i]
	if count > max_letters:
		longest_name = name
		max_letters = count

print(longest_name)

#use zip instead

for name, count in zip(names, letters):
	if count > max_letters:
		longest_name = name
		max_letters = count

print(longest_name)

#zip will not work in python 2, use itertools instead
#zip can behave strangely

names.append('Rosalind')
for name, count in zip(names, letters):
	print(name)

#zip truncates if iterators of different lengthes
#see page 23 of effective python