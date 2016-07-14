a=int(input())
b = [int(input()) for x in range(a)]
for i in range(len(b)):
	for j in range(len(b)):
		if b[i]==b[j] and i!=j:
			break
	else: print(b[i])
