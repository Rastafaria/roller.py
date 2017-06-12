# roller.py
Simple CLI tool for simulating dice rolls and obtaining useful information from it. Meant for tabletop games with lots of rolling.

# Usage: 
python roller.py [-h] [--count comparator comparand] [--filter comparator comparand] [--reroll comparator comparand] rolls size

count: Specify whether or not to count and with what criteria. First argument is a string [">","<","=",">=","<="] denoting which comparator to use, and second argument is an integer to compare rolls to.

filter: Hides all rolls that do not meet the criteria. Will not hide first set of rolls if rerolling. First argument is a string [">","<","=",">=","<="] denoting which comparator to use, and second argument is an integer to compare rolls to.

reroll: Allows you to do a second batch of rolls on rolls that meet the criteria. First argument is a string [">","<","=",">=","<="] denoting which comparator to use, and second argument is an integer to compare rolls to.

rolls: The amount of dice to be rolled. Argument is an integer.

size: Amount of sides on the dice to be rolled. Argument is an integer.

# Examples:

$python roller.py 10 6
>[3, 1, 6, 5, 3, 1, 1, 2, 5, 6]

This will roll 10 six-sided dice and display the results.

$python roller.py --count ">" 3 10 6
>[2, 1, 3, 3, 2, 3, 1, 3, 5, 4]
>Number of matches: 2

This will roll 10 six-sided dice, display the results, then count all the dice whose result is greater than 3 and display the counted amount.

$python roller.py --filter ">" 1 10 6
>[5, 4, 6, 5, 3, 6, 4, 4, 6]

This will roll 10 six-sided dice, and display the results, hiding the dice of result 1.

$python roller.py --reroll "=" 1 10 6
>[3, 3, 5, 5, 4, 2, 6, 2, 6, 1]

>[3, 3, 5, 5, 4, 2, 6, 2, 6, 6]

This will roll 10 six-sided dice, display the results, reroll all results that equal 1, and display the second set with the rerolls. The rerolls are at the end of the set.

$python roller.py --count ">" 3 --reroll "=" 1 10 6
>[5, 6, 2, 1, 2, 1, 2, 2, 6, 3]

>Number of matches: 3

>[5, 6, 2, 2, 2, 2, 6, 3, 4, 5]

>Number of matches after reroll: 5

This will roll 10 six-sided dice, display results and count, reroll, then display the second set and count.

$python roller.py --count ">" 3 --filter ">" 3 --reroll "=" 1 10 6
>[3, 1, 1, 1, 1, 5, 5, 6, 1, 4]

>Number of matches: 4

>[5, 5, 6, 4, 4, 4, 6]

>Number of matches after reroll: 7

This will roll 10 six-sided dice, display the results and count, then reroll and filter the second set and finally display that set and its count.
