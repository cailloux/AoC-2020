data = [line.strip() for line in open('./input/day14.in')]

def computeNumber(mask, number):
    value = ''
    mask = str(mask)
    number = str(number)
    for i, bit in enumerate(number): 
        if mask[i] == 'X':
            value += bit
        elif mask[i] == '1':
            value += '1'
        elif mask[i] == '0':
            value += '0'
    return value


memory = {}
mask = value = address = ''

answer = 0
for line in data:

    if line.startswith('mask'):
        mask = line.split('=')[1].strip()
    else:
        address, value = line.split('=')
        address = address.strip()
        address = int(address[4:-1])
        value = int(value)
        value = bin(value)[2:].zfill(36)
        memory[address] = int(computeNumber(mask, value),2)

answer = sum(memory.values())

print(answer)
