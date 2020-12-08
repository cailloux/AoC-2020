import re

f = open("./input/day7.in", "r")

TARGET_COLOR = "shiny gold"
rules = []
contents = {}


def find(bagColor, targetBag):
    return bagColor == targetBag or any([find(x[1], targetBag) for x in contents[bagColor]])

def bagSize(bagColor):
    return sum([bag[0] + bag[0] * bagSize(bag[1]) for bag in contents[bagColor]])


for line in f:
    rules.append(line.strip())

for rule in rules:
    bag, containedBags = rule.split('contain')

    subBags = containedBags.split(",")

    i = 0
    while i < len(subBags):
        subBags[i] = subBags[i].strip()
        i += 1

    subContainedBags = []
    for x in subBags:
        subContainedBags.append(re.match("(\d)\s([\s\w]+)\s((bags)|(bag))", x))

    finalBagList = []
    for j in subContainedBags:
        if j:
            finalBagList.append((int(j.group(1)), j.group(2)))

    contents[bag.split('bags')[0].strip()] = finalBagList


print(sum([bag[0] + bag[0] * bagSize(bag[1]) for bag in contents[TARGET_COLOR]]))
