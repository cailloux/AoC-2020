customsGroupAnswers = open("./input/day6.in", "r").read().split("\n\n")

part2 = 0

for partyAnswers in customsGroupAnswers:
    unique = {}
    partyCount = len(partyAnswers.splitlines())
    for char in partyAnswers:
        if char not in unique and char != '\n':
            unique[char] = 1
        elif char != '\n':
            unique[char] += 1
    for x in unique:
        if partyCount == unique[x]:
            part2 += 1

print("Part 2:", part2)
