#Item 13: Take advantage of of each block in try/except/else/finally
#go straight to bottom.

'''
#Finally blocks
handle = open('random_data.txt')
try: 
	data = handle.read()
finally: 
	handle.close()

print(data)

def load_json_key(data, key):
	try:
		result_dict = json.loads(data)
	except ValueError as e:
		raise KeyError from e
	else:
		return result_dict[key]
'''

'''
#from python3 documentation
while True:
	try:
		x = int(input("Please enter a number"))
		break
	except ValueError:
		print("Oops! that is not a number")
'''

'''
>>> def divide(x, y):
...     try:
...         result = x / y
...     except ZeroDivisionError:
...         print("division by zero!")
...     else:
...         print("result is", result)
...     finally:
...         print("executing finally clause")
...
>>> divide(2, 1)
result is 2.0
executing finally clause
>>> divide(2, 0)
division by zero!
executing finally clause
>>> divide("2", "1")
executing finally clause
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in divide
TypeError: unsupported operand type(s) for /: 'str' and 'str'
'''

#everything together good practice
UNDEFINED = object()
def divide_json(path):
	handle =open(path, 'r+') #may raise an exception error
	try:
		data = handle.read() #may raise UnicodeDecodeError
		op = json.loads(data) #may raise ValueError
		value = (
			op['numerator'] /
			op['denomiator']) #may raise ZeroDivisionError
	except ZeroDivisionError as e:
		return UNDEFINED
	else:
		op['result'] = value
		result = json.dumps(op)
		handle.seek(0)
		handle.write(result) #may raise IOError
		return value
	finally:
		handle.close() #always runs

