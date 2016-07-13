a=int(input())
b=int(input())
c=[]
while a>0:
	x=a%10
	a=int(a/10)
	c.append(x)
c=sorted(c)
x=0
for i in range(b):
	del c[len(c)-1]
for i in range(len(c)):
	x=(x*10)+c[i]
print(x)
