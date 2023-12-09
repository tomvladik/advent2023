inputString = open('03/input.txt', 'r').read()

debug = False  # change to get debug outputs
def dbgPrint(message):
    if debug:
        print(message)


theSum = 0
asterisksMap = {}
lines = inputString.splitlines()
totalLines = len(lines)


def isOk(char):
    return char == "*"


def isPositionInLineOk(i, line):
    if line is not None:
        cnt = len(line)
        if isOk(line[i]):
            return i
        if i > 0 and isOk(line[i - 1]):
            return i - 1
        if i < cnt - 1 and isOk(line[i + 1]):
            return i + 1
    return None


def isPositionOk(r, c):
    x = isPositionInLineOk(c, lines[r])
    if x is not None:
        return (r, x)
    if r > 0:
        x = isPositionInLineOk(c, lines[r - 1])
        if x is not None:
            return (r - 1, x)
    if r < totalLines - 1:
        x = isPositionInLineOk(c, lines[r + 1])
        if x is not None:
            return (r + 1, x)
    return None


def addValueToMap(address, value):
    a = asterisksMap.get(address, None)
    if a is None:
        a = []
        asterisksMap[address] = a
    a.append(value)


# Iterate over the lines
for i, line in enumerate(lines):
    dbgPrint(line)
    currentNumber = ""
    asterisk = None

    for j, character in enumerate(line):
        if character.isdigit():
            currentNumber += character
            if asterisk is None:
                asterisk = isPositionOk(i, j)
        else:
            if currentNumber != "" and asterisk is not None:
                addValueToMap(asterisk, int(currentNumber))
                dbgPrint(f"number: {currentNumber} {asterisk}")
            currentNumber = ""
            asterisk = None
    if currentNumber != "" and asterisk is not None:
        addValueToMap(asterisk, int(currentNumber))
        dbgPrint(f"number: {currentNumber} {asterisk}")

for key, value in asterisksMap.items():
    if len(value) >= 2:
        multi = 1
        for n in value:
            multi *= n
        theSum += multi

print(f"**** RESULT: {theSum} ****")
