a=int(input())
b = [int(input()) for x in range(a)]
elementfound=0
for i in range(len(b)):
	if elementfound==0:
		for j in range(len(b)):
			if b[i]==b[j] and i!=j:
				print(b[i])
				elementfound=1
