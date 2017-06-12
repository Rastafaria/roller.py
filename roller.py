import argparse
import random as rand

global compsign
compsign = '='

def roll(n):
    return rand.choice(range(1,n+1))

def parseComparation(argList):
    comparator, comperand = argList
    comperand = int(comperand)
    if comparator == '>':
        def comparatorf(a,b):
            return a > b
        compsign = '>'
        return comparatorf, comperand
    elif comparator == '<':
        def comparatorf(a,b):
            return a < b
        compsign = '<'
        return comparatorf, comperand
    elif comparator == '=':
        def comparatorf(a,b):
            return a == b
        compsign = '='
        return comparatorf, comperand
    elif comparator == '>=':
        def comparatorf(a,b):
            return a >= b
        compsign = '>='
        return comparatorf, comperand
    elif comparator == '<=':
        def comparatorf(a,b):
            return a <= b
        compsign = '<='
        return comparatorf, comperand
    else:
        raise Exception('no')

def batchRoll(rolls, size):
    return [roll(size) for _ in range(rolls)]

def countBatch(batch, comparator, comperand):
    count = 0
    for n in batch:
        if comparator(n, comperand):
            count += 1
    return count

def filterBatch(batch, comparator, comperand):
    newList = []
    for n in range(len(batch)):
        if (comparator(batch[n], comperand)):
            newList.append(batch[n])
    return newList

def rerollBatch(batch, comparator, comperand, size):
    count = 0
    for n in batch:
        if comparator(n, comperand):
            count += 1
    if compsign == '=':
        def c(a,b):
            return a != b
        comparator = c
    newList = filterBatch(batch, comparator, comperand)
    for _ in range(count):
        newList.append(roll(size))
    return newList
parser = argparse.ArgumentParser(description='Simple dice roller with filtering and rerolling capabilities.')
parser.add_argument('rolls', metavar='Rolls', type=int,
                    help='The amount of dice to be rolled. Argument is an integer.')
parser.add_argument('size', metavar='dieSize', type=int,
                    help='Amount of sides on the dice to be rolled. Argument is an integer.')
parser.add_argument('--count', action='store', nargs=2,
                    help='Specify whether or not to count and with what criteria. First argument is a string [">","<","=",">=","<="] denoting which comparator to use, and second argument is an integer to compare rolls to.')
parser.add_argument('--filter', action='store', nargs=2,
                    help='Hides all rolls that do not meet the criteria. Will not hide first set of rolls if rerolling. First argument is a string [">","<","=",">=","<="] denoting which comparator to use, and second argument is an integer to compare rolls to.')
parser.add_argument('--reroll', action='store', nargs=2,
                    help='Allows you to do a second batch of rolls on rolls that meet the criteria. First argument is a string [">","<","=",">=","<="] denoting which comparator to use, and second argument is an integer to compare rolls to.')
args = parser.parse_args()

#Check for Nones
counting = True if args.count != None else False
filtering = True if args.filter != None else False
rerolling = True if args.reroll != None else False

if counting:
    countfunc, countnum = parseComparation(args.count)
if filtering:
    filterfunc, filternum = parseComparation(args.filter)
if rerolling:
    rerollfunc, rerollnum = parseComparation(args.reroll)

batch = batchRoll(args.rolls, args.size)

if filtering and not rerolling:
    print(filterBatch(batch, filterfunc, filternum))
else:
    print(batch)

if counting:
    print('Number of matches: ' + str(countBatch(batch, countfunc, countnum)))

if rerolling:
    batch2 = rerollBatch(batch, rerollfunc, rerollnum, args.size)
    if filtering:
        print(filterBatch(batch2, filterfunc, filternum))
    else:
        print(batch2)

    if counting:
        print('Number of matches after reroll: ' + str(countBatch(batch2, countfunc, countnum)))