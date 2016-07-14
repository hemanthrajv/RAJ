c = int(input())
d = [int(input()) for x in range(c)]
for i in range(len(d)):
	for j in range(len(d)):
		if d[i]==d[j] and i!=j:
			break
	else: print(d[i])
