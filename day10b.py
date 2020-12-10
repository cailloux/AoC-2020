adapters = [int(line.strip()) for line in open('./input/day10.in', 'r')]

adapters.append(0)
adapters = sorted(adapters)

configuration = [1] + [0] * (len(adapters) - 1)
for i, adapter in enumerate(adapters):
    for j in range(i - 3, i):
        if(adapter - adapters[j] <= 3):
            configuration[i] += configuration[j]

answer = configuration[-1]
print(answer)
