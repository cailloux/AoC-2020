f = open("day2.in","r")


validCount = 0
targetLetter = ''

def passwordValidator(letter, range, password):
	isValid = False
	count = 0
	
	validRange = range.split('-')
	validRange[0] = int(validRange[0]) - 1
	validRange[1] = int(validRange[1]) - 1
	
	for x in validRange:
		if letter == password[x]:
			count += 1

	if count == 1:
		isValid = True
	
	return isValid

for x in f:
	x = x.rstrip()
	values = x.split()
	targetLetter = values[1]
	targetLetter = targetLetter[0]
	if passwordValidator(targetLetter, values[0], values[2]):
		validCount += 1

print(validCount)