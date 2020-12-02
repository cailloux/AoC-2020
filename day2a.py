f = open("day2.in","r")

# 1-3 a: abcde
# 1-3 b: cdefg
# 2-9 c: ccccccccc

validCount = 0
targetLetter = ''

def passwordValidator(letter, range, password):
	isValid = False
	count = 0
	count = password.count(letter)
	
	validRange = range.split('-')
	
	
	
	# print(int(validRange[0]))
	# print(int(validRange[1]))
	# print(letter)
	# print(password)
	
	if int(validRange[0]) <= count <= int(validRange[1]):
		isValid = True
		print("Valid")
	return isValid

for x in f:
	x = x.rstrip()
	values = x.split()
	print(values)
	targetLetter = values[1]
	targetLetter = targetLetter[0]
	if passwordValidator(targetLetter, values[0], values[2]):
		validCount += 1

print(validCount)