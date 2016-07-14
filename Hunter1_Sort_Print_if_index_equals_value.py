def index():
	a=int(input())
	b = [int(input()) for x in range(a)]
	b = sorted(b)
	for i in range(len(b)):
		if i==b[i]:
			print(b[i]," is equal to its index ",i)
index()
