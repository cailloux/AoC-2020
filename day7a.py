import re

f = open("./input/day7.in", "r")

TARGET_COLOR="shiny gold"
rules = []
contents = {}

def findBag(bagColor, targetBag):
    return bagColor == targetBag or any([findBag(x[1], targetBag) for x in contents[bagColor]])

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


print(sum([any([findBag(bag[1], TARGET_COLOR) for bag in contents[rule]])
           for rule in contents]))
