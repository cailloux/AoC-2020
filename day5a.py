f = open('day5.in', 'r')

def getSeatId(row, column):
    i = 0
    j = 0
    dropper = 0
    rows = []
    columns = []

    while i < 128:
        rows.append(i)
        i += 1

    while j < 8:
        columns.append(j)
        j += 1

    for x in row:
        dropper = int(len(rows) / 2)
        if x == "F":
            rows = rows[:dropper]
        elif x == "B":
            rows = rows[dropper:]
    

    for x in column:
        dropper = int(len(columns) / 2)
        if x == "L":
            columns = columns[:dropper]
        elif x == "R":
            columns = columns[dropper:]

    return int(rows[0]) * 8 + int(columns[0]) 


rowString = ""
columnString = ""
seatId = []

for line in f:
    line = line.rstrip()
    rowString = line[:7]
    columnString = line[7:]
    seatId.append(getSeatId(rowString, columnString))

print("Part 1:", max(seatId))
f.close()
