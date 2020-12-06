import re

customsGroupAnswers = open("day6.in", "r").read().split("\n\n")

# customsGroupAnswers = ['abc', 'a\nb\nc\n', 'ab\nac\n', 'a\na\na\na\n', 'b\n']

part1 = 0

for partyAnswers in customsGroupAnswers:
    unique = []
    partyAnswers = partyAnswers.strip("\n")
    for char in partyAnswers[::]:
        if char not in unique and char != '\n':
            unique.append(char)
    part1 += len(unique)

print("Part1: ", part1)
