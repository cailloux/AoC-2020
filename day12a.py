data = [line.strip() for line in open('./input/day12.in')]

x = 0
y = 0
heading = 90

for instruction in data:
    command = instruction[0]
    magniutde = int(instruction[1:])

    if command == 'N':
        y = y + magniutde
    elif command == 'S':
        y = y - magniutde
    elif command == 'E':
        x = x + magniutde
    elif command == 'W':
        x = x - magniutde
    elif command == 'L':
        heading = heading - magniutde
        if heading < 0:
            heading = heading + 360
    elif command == 'R':
        heading = heading + magniutde
        if heading >=360:
            heading = heading - 360
    elif command == 'F':
        if heading == 0:
            y = y + magniutde
        elif heading == 90:
            x = x + magniutde
        elif heading == 180:
            y = y - magniutde
        elif heading == 270:
            x = x - magniutde

answer = abs(x) + abs(y)

print(answer)
