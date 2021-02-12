import itertools
import random

# def waarin de bot net zolang het aantal combinaties blijft verkleinen todat er maar 1 mogenlijk is
def bot():
    def firstguess():
        guess1 = combinations[random.randint(0, len(combinations) - 1)]
        return list(guess1)


    def controleren(quess, geheimecode):
        goedfout = [0, 0]
        copy = quess[:]
        codecopy = geheimecode[:]
        for value in range(0, len(quess)):
            if quess[value] == geheimecode[value]:
                goedfout[0] += 1
                copy.pop(value)
                copy.insert(value, 'None')
                codecopy.pop(value)
                codecopy.insert(value, 'enoN')

        for value in range(0, len(copy)):
            if copy[value] in codecopy:
                goedfout[1] += 1
                codecopy.remove(copy[value])
                codecopy.insert(value, 'enoN')

        return goedfout


    def eruit(mogenlijkheden, gok, goedfout):
        coderesult = [0, 0]

        resultaat = []
        for possiblecode in mogenlijkheden:
            if goedfout == controleren(gok, possiblecode):
                resultaat.append(possiblecode)
        return resultaat

    possiblecolours = ['red', 'pink', 'yellow', 'green', 'orange', 'blue']
    combinations = list(itertools.product(possiblecolours, repeat=4))
    mogenlijkheden = []
    for option in combinations:
        mogenlijkheden.append(list(option))


    def secretcode():
        colours = ['red', 'pink', 'yellow', 'green', 'orange','blue']
        colourcode = []

        for value in range(0, 4):
            colourcode.append(random.choice(colours))
        return colourcode

    geheimecode = secretcode()



    eerstegok = firstguess()
    goedfout = controleren(eerstegok, geheimecode)
    options = eruit(mogenlijkheden, eerstegok, controleren(eerstegok, geheimecode))
    # print(options)
    label = []

    while goedfout != [4, 0]:
        randomchoice = random.choice(options)
        options = eruit(options, randomchoice, controleren(randomchoice, geheimecode))
        goedfout = controleren(randomchoice, geheimecode)
        label.append(goedfout)
        label.append(len(options))
        print(goedfout)
        print(len(options))
    return label

class label:
    def __init__(self):
        return

    def labeltje(self):
        self.label = bot()
        print(self.label)
        return self.label

