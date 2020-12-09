data = [int(line.strip()) for line in open('./input/day9.in')]

preamble = data[:25]
data = data[25:]
hits = []
misses = []

def battleship(intList, target):
    miss = 0
    for n1 in intList:
        for n2 in intList:
            if n1 + n2 == target:
                return target, True
            if n1 + n2 != target:
                miss = target
    if miss == target:
        return target, False

for i, target in enumerate(data):

    answer, found = battleship(preamble, target)

    if found:
        hits.append(answer)
    elif not found:
        misses.append(answer)
    preamble.append(data[i])
    preamble.pop(0)

print(misses[0])
