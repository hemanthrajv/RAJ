x=int(input())
b=int(0)
for n in range(2, x):
     for x in range(2, n):
         if n % x == 0:
             break
     else:
         b+=1
print("The number of prinme numbers available:",b)
