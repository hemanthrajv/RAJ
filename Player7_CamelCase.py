a=input()
b=''.join([ch for ch in a.title() if not ch.isspace()])
print(b)
