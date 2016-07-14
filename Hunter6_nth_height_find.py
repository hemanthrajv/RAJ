a=[int(input()) for i in range(50)]
a=sorted(a)
print("The height of 4th tallest is",a[45])
print("To find the nth tallest, enter n:")
print("Height:",a[(int(input()))-1])
