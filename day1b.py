targetValue = 2020
expenses = []
total = 0

f = open("./input/day1.in","r")

for x in f:
	x = x.rstrip()
	expenses.append(x)

for i in expenses:
	for j in expenses:
		for k in expenses:
			answer = 0
			a = int(i)
			b = int(j)
			c = int(k)
			total = a + b + c
			if total == targetValue:
				answer = a * b * c
				print("1st number is: ", a)
				print("2nd number is: ", b)
				print("3rd number is: ", c)
				print("Answer is: ", answer)
				break
		if total == targetValue:
			break
	if total == targetValue:
		break