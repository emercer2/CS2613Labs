def wordsOfGivenLen(sentance, wordLen):
	words = sentance.split(" ")
	wordsOfNLen = []
	for i in range(len(words)):
		if len(words[i]) == wordLen:
			wordsOfNLen.append(words[i])
	return wordsOfNLen
	
def longestWords(sentance):
	words = sentance.split(" ")
	maxLen = 0;
	longestWords = []
	for i in range(len(words)):
		if len(words[i]) > maxLen:
			maxLen = len(words[i])
			
	for i in range(len(words)):
		if len(words[i]) == maxLen:
			longestWords.append(words[i])
	return longestWords
	
def commonLetter(sentance):
	words = sentance.lower().split(" ")
	letterCounts = [0] * 26
	
	for i in range(len(words)):
		for j in words[i]:
			if ord(j) >= 97 and ord(j) <= 122:
				letterCounts[ord(j)-97] += 1
				
	maxCount = 0;
	for i in range(len(letterCounts)):
		if letterCounts[i] > maxCount:
			maxCount = letterCounts[i]
			
	mostCommon = []
	if maxCount != 0:
		for i in range(len(letterCounts)):
			if letterCounts[i] == maxCount and mostCommon.count(chr(letterCounts[i]+97)) == 0:
				mostCommon.append(chr(i+97))
	else:
		mostCommon = "No most common letter found."
	return mostCommon
	
print(wordsOfGivenLen("The white cat and the red fox.", 3))
print(wordsOfGivenLen("The white carrot cat orange monkey here and carrot the red fox.", 6))

print(longestWords("Hello CS2613! Python is fun."))
print(longestWords("Hello CS2613 - Python is fun."))

print(commonLetter("My name is…"))
print(commonLetter("This is!"))
