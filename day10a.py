adapters = [int(line.strip()) for line in open('./input/day10.in', 'r')]

adapters = sorted(adapters)
adapters.append(max(adapters) + 3)
maxInputJoltage = max(adapters)
oneJoltAdapters = []
twoJoltAdapters = []
threeJoltAdapters = []
currentJoltage = 0
currentAdapter = 0

while currentJoltage < maxInputJoltage:

    if adapters[0] - 1 == currentJoltage:
        currentAdapter = adapters[0]
        adapters.remove(currentAdapter)
        oneJoltAdapters.append(currentAdapter)
    # No 2-step jump
    # elif adapters[0] - 2 == currentJoltage:
    #     currentAdapter = adapters[0]
    #     adapters.remove(currentAdapter)
    #     twoJoltAdapters.append(currentAdapter)
    elif adapters[0] - 3 == currentJoltage:
        currentAdapter = adapters[0]
        adapters.remove(currentAdapter)
        threeJoltAdapters.append(currentAdapter)
    currentJoltage = currentAdapter

# threeJoltAdapters.append(maxInputJoltage[-1])
# 2574

print(len(oneJoltAdapters) * len(threeJoltAdapters))
