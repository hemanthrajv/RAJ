a=int(input())
x=[int(input()) for i in range(a)]
b=int(input())
y=[int(input()) for j in range(b)]
if set(x)<set(y):
	print("A is a sub set of B")
