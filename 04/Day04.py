inputString = open("04/input.txt", "r").read()

debug = True  # change to get debug outputs
def dbgPrint(message):
    if debug:
        print(message)

theSum = 0
lines = inputString.splitlines()

# Iterate over the lines
for line in lines:
    name, cards = line.split(":")
    dbgPrint(name)
    dbgPrint(cards)

    wining, guesses = cards.split("|")
    wining = list(map(int, wining.split()))
    guesses = list(map(int, guesses.split()))
    dbgPrint(f".. wining  : {wining}")
    dbgPrint(f".. guesses : {guesses}")
    intersection = list(set(wining) & set(guesses))
    dbgPrint(f".. intersection : {intersection}")
    number = len(intersection)
    if number > 1:
        number = 2 ** (len(intersection) - 1)
    dbgPrint(number)
    theSum += number

print(f"**** RESULT: {theSum} ****")
