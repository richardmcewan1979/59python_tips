#This is an example of a list comrehension
value = [len(x) for x in open('my_file.txt')]
print(value)

#generator expressions very fast
#evaulate to an iterator one item at a time.
it = (len(x) for x in open('my_file.txt'))
print(it)
print(next(it))
print(next(it))

#we can use this in another generator
roots =((x,x**0.5) for x in it)
print(next(roots))
print(next(roots))

#generators are stateful so use only once



