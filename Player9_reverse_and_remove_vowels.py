a=input()
b=[ch for ch in a]
c=[]
for i in range(len(b)):
	c.append(b[int(len(b)-1)-i])
print(''.join(c))
j=0
while j<len(c):
	if (c[j]=='a' or c[j]=='e' or c[j]=='o' or c[j]=='i' or c[j]=='u'):
		del c[j]
	j=j+1
print(''.join(c))
