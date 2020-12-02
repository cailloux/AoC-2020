targetValue = 2020

f = open("day1.in","r")
expenses = []

for x in f:
	x = x.rstrip()
	expenses.append(x)


for i in expenses:
	total = 0
	for j in expenses:
		answer = 0
		a = int(i)
		b = int(j)
		total = a + b
		if total == targetValue:
			answer = a * b
			print("1st number is: ", a)
			print("2nd number is: ", b)
			print("Answer is: ", answer)
			break
	if total == targetValue:
		break