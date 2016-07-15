def workingday(x):
	c=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
	for x in c:
		if x==c[0]:
			return "True"
		else:
			return "False"
print(workingday(input()))
