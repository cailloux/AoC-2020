f = open('./input/day13.in', 'r')

earliestTime = int(f.readline().strip())
buses = f.readline().strip().split(',')

busTime = []
nextArrival = {}

for bus in buses:
    if bus != 'x':
        busTime.append(int(bus))

busTime = sorted(busTime)

for bus in busTime:
    nextArrivalTime = int(earliestTime / bus) * bus + bus
    nextArrival[bus] = int(nextArrivalTime - earliestTime)

quickestBus = min(nextArrival, key=nextArrival.get)
print(quickestBus * nextArrival[quickestBus]) 
