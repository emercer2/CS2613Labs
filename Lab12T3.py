import math

timesTwo = lambda num : num*2
	
charAtCen = lambda str : str[math.floor((len(str)-1)/2)]

isOddPos = lambda val : True if (val % 2 == 1) and (val >= 0) else False

startWithVow = lambda str : True if (str[0] == "a") or (str[0] == "e") or(str[0] == "i") or (str[0] == "o") or(str[0] == "u") or (str[0] == "A") or (str[0] == "E") or(str[0] == "I") or (str[0] == "O") or(str[0] == "U") else False

print(list(map(timesTwo, [8, 10, 7.5])))
print(list(map(charAtCen, ["Hello!", "CompSci2613", "Lab-12"])))
print(list(filter(isOddPos, [-15, -4, 0, 4, 23, 64, 101, 104, 123])))
print(list(filter(startWithVow, ["alice", "bob", "Carl", "daisy", "Earl"])))
