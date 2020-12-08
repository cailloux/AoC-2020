import copy

with open('day8.in') as f:
    program = [line.strip() for line in f]

def execute(program):

    step = 0
    acc = 0
    executed = []

    while (True):
        if step >= len(program):
            return (acc, False)

        if step in executed:
            return (acc, True)

        instruction = program[step].split(' ')[0]
        value = int(program[step].split(' ')[1])
        executed.append(step)

        if instruction == 'acc':
            acc += value
            step += 1
        elif instruction == 'nop':
            step += 1
        elif instruction == 'jmp':
            step += value


looping = False

i = 0
while i < len(program):
    programCopy = copy.deepcopy(program)

    instruction = programCopy[i].split(' ')

    if instruction[0] == 'nop':
        programCopy[i] = 'jmp ' + str(instruction[1])
    elif instruction[0] == 'jmp':
        programCopy[i] = 'nop ' + str(instruction[1])

    (acc, looping) = execute(programCopy)
    if not looping:
        print(acc)
        break
    i += 1

