with open('./input/day8.in') as f:
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


print(execute(program)[0])
