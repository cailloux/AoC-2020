data = [int(line.strip()) for line in open('./input/day9.in')]
target = 104054607

targetRange = 2

while True:
    j = 0
    x = 0
    while (j + targetRange) <= len(data):
        amItheAnswer = 0
        attempts = []
        for i in range(targetRange):
            x = i + j
            amItheAnswer += data[x]
            attempts.append(data[x])
        if amItheAnswer == target:
            targetSum = min(attempts) + max(attempts)
            print(targetSum)
            break
        j += 1
    if amItheAnswer == target:
        break

    targetRange += 1
