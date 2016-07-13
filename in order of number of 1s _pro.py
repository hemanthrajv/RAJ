print("Enter the number of values in array:")
a=int(input())
b=[]
for i in range(a):
	b.append([])
	b[i].append(int(input()))
	b[i].insert(0,(bin(int(b[i][0])).count("1")))
b=sorted(b)
for i in range(a): 	print(b[a-1-i][1])
