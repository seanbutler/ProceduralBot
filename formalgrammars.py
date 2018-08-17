# DERIVED FROM CODE FOUND HERE...
# https://eli.thegreenplace.net/2010/01/28/generating-random-sentences-from-a-context-free-grammar

import random

class ContextFreeGrammar:
    def __init__(self):
        self.prod = {}

    def AddRule(self, lhs, rhs):
        self.prod.update({lhs:rhs})

    def GenerateRandom(self, symbol):
        sentence = []

        randomchoice = self.prod[symbol]
        randomchoice = random.choice(self.prod[symbol])
        randomchoicelist = randomchoice.split(' ')

        for sym in randomchoicelist:            # for each symbol in the RHS
            if sym in self.prod:                # if its a NON TERMINAL (i.e. another LHS)
                sentence.append(self.GenerateRandom(sym))
            else:
                sentence.append(sym)

        return sentence
