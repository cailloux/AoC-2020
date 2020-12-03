f = open("day3.in","r")

x = y = 0
trees = 0
xStep = 2
yStep = 1
i = 0

def hitTheTree(line, position):
	tree = False
	if line[position] == "#":
		tree = True
	return tree


for line in f:
	# Skip the first line, because we're stepping down and not considering it
	if i == 0:
		i += 1
		continue
	elif i % xStep != 0:
		i += 1
		continue

	line = line.rstrip()
	
	y += yStep
	if y >= len(line):
		y = y - len(line)

	if hitTheTree(line, y):
		trees += 1
	i += 1

f.close()
print(trees)