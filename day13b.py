from functools import reduce

f = open('./input/day13.in', 'r')

earliestTime = int(f.readline().strip())
buses = f.readline().strip().split(',')


def valid_answer(n, mod, answer):
    return (n+answer) % mod == 0

def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1

def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


busIds = []
timeOffset = []

for i, busId in enumerate(buses):
    if busId != "x":
        busId = int(busId)
        busIds.append(busId)
        timeOffset.append(busId - i)

answer = chinese_remainder(busIds, timeOffset)

print(answer)
