'''
Question:
Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys. The function should just print the keys only.
'''
def dic(lower,upper):
	d = {}
	for i in range(lower,upper+1):
		d[i] = i*i
	for (keys,values) in d.items():
		print(keys)

dic(1,20)
