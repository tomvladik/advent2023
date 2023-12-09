inputString = open("04/input.txt", "r").read()

lines = inputString.splitlines()
winPlan = {}

# Iterate over the lines
for line in lines:
    name, cards = line.split(":")
    _, cardNumber = name.split()
    cardNumber = int(cardNumber)
    wining, guesses = cards.split("|")
    wining = list(map(int, wining.split()))
    guesses = list(map(int, guesses.split()))

    intersection = list(set(wining) & set(guesses))
    count = len(intersection)

    copies = list(range(cardNumber + 1, cardNumber + count + 1))
    winPlan[cardNumber] = copies

theSum = 0
linesCnt = len(winPlan)
for i in range(linesCnt, 0, -1):
    addCopies = winPlan[i].copy()
    for j in winPlan[i]:
        if j <= linesCnt:
            addCopies += winPlan[j]
    winPlan[i] = addCopies
    theSum += 1 + len(addCopies)
print(f"**** RESULT: {theSum} ****")
