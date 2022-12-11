import re
from math import prod

class Monkey:
    def __getInts(self,txt):
        return [int(s) for s in re.findall(r'\b\d+\b', txt)]

    def __init__(self,items,operation,test) -> None:
        self.items = self.__getInts(items)
        self.operation = eval("lambda old: " + operation.split(" = ")[1])
        throwTest = [self.__getInts(opp)[0] for opp in test]
        self.test = lambda item: throwTest[1] if item%throwTest[0]==0 else throwTest[2]
        self.inspected = 0

class MonkeyInTheMiddle:
    def __init__(self,input) -> None:
        self.monkeys = []
        self.mod = 1 # This will take the item values modulo an appropriate value
        for ind in [i for i,d in enumerate(input) if 'Monkey' in d]:
            self.monkeys.append( Monkey(input[ind+1],input[ind+2],input[ind+3:ind+6]) )
            self.mod *= int(input[ind+3].split(' ')[-1])

    def advanceRound(self,worryFactor):
        for monkey in self.monkeys:
            while len(monkey.items) > 0:
                item = monkey.items.pop(0)
                monkey.inspected += 1
                item = monkey.operation(item)
                item = item//worryFactor % self.mod
                self.monkeys[monkey.test(item)].items.append( item )


# The trick to part 2 is to realize that a monkey does not actually care about an item's raw worry value;
# it only cares about its value modulo its divisibility condition. Thus, if we take all item values modulo
# the product of the divisors in the monkey divisibility criterions, how the monkeys throw them around will
# be exactly the same, but we will have far smaller numbers now.
def Part1(data):
    monkeyGame = MonkeyInTheMiddle(data)
    for _ in range(20):
        monkeyGame.advanceRound(3)
    return prod(sorted(m.inspected for m in monkeyGame.monkeys)[-2:])

def Part2(data):
    monkeyGame = MonkeyInTheMiddle(data)
    for _ in range(10000):
        monkeyGame.advanceRound(1)
    return prod(sorted(m.inspected for m in monkeyGame.monkeys)[-2:])