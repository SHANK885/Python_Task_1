'''
Write a program to compute 1/2+2/3+3/4+...+n/n+1
with a given n input by console (n>0).
'''
n = int(input("Enter the value of N : "))
sum = 0.0
for i in range(1,n+1):
	sum += float(float(i)/(i+1))
print(round(sum,2))
