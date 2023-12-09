inputString = open('03/input.txt', 'r').read()

debug = False  # change to get debug outputs

def dbgPrint(message):
    if debug:
        print(message)


theSum = 0
lines = inputString.splitlines()


def isOk(char):
    return char != "." and not char.isdigit()


def isPositionInLineOk(i, line):
    if line is not None:
        cnt = len(line)
        if (
            isOk(line[i])
            or i > 0
            and isOk(line[i - 1])
            or i < cnt - 1
            and isOk(line[i + 1])
        ):
            return True
    return False


def isPositionOk(i, curLin, prevLin, folLin):
    return (
        isPositionInLineOk(i, curLin)
        or isPositionInLineOk(i, prevLin)
        or isPositionInLineOk(i, folLin)
    )


# Iterate over the lines
totalLines = len(lines)
for i, line in enumerate(lines):
    previousLine = lines[i - 1] if i > 0 else None
    followingLine = lines[i + 1] if i < totalLines - 1 else None

    dbgPrint(line)
    currentNumber = ""
    enabled = False

    for j, character in enumerate(line):
        dbgPrint(character)
        if character.isdigit():
            currentNumber += character
            enabled = enabled or isPositionOk(j, line, previousLine, followingLine)
        else:
            dbgPrint(f"number: {currentNumber} {enabled}")
            if currentNumber != "" and enabled:
                theSum += int(currentNumber)
            currentNumber = ""
            enabled = False
    if currentNumber != "" and enabled:
        theSum += int(currentNumber)

print(f"**** RESULT: {theSum} ****")
