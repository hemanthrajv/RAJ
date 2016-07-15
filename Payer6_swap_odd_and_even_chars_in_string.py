c=input()
b=[ch for ch in c]
i=int(0)
while i<=(len(b)-1):
	ch=b[i]
	b[i]=b[i+1]
	b[i+1]=ch
	i=i+2
c=''.join(b)
print(c)
