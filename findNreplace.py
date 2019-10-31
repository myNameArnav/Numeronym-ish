sentence = 'hate in the nation'
sentenceSplit = ['hate', 'in', 'the', 'nation']
pspelling = ['heɪt', 'ɪn', 'ðə', 'ˈneɪʃ(ə)n']
numPspelling = ['wʌn', 'tuː', 'θriː', 'fɔː', 'fʌɪv',
				'sɪks', 'ˈsɛv(ə)n', 'eɪt', 'nʌɪn', 'ˈzɪərəʊ']
space = " "
nospace = ""
wordMatch = []
#numspelling = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'zero']
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
#combined = {'1': 'wʌn', '2': 'tuː', '3': 'θriː', '4': 'fɔː', '5': 'fʌɪv','6': 'sɪks', '7': 'ˈsɛv(ə)n', '8': 'eɪt', '9': 'nʌɪn', '0': 'ˈzɪərəʊ'}

#----------Logic-----------#
i, j, a, b, c = 0, 0, 0, 0, 0
for i in range(len(pspelling)):
	singleWordno = nospace.join(pspelling[i]).split()
	singleWord = space.join(pspelling[i]).split()
	print("<      " + str(singleWord))
	for j in range(len(numPspelling)):
		singleNum = space.join(numPspelling[j]).split()
		singleNumno = nospace.join(numPspelling[j]).split()
		# print(singleNum)
		wordMatch = []
		for a in range(len(singleNum)):
			for b in range(len(singleWord)):
				if len(singleNum) <= len(singleWord):
					if singleNum[a] == singleWord[b]:
						wordMatch.extend(singleNum)
						if len(wordMatch) >= 3:
							for c in range(len(numPspelling)):
								if "".join(str(wordMatch)) == "".join(str(numPspelling[c])):
									print(wordMatch)
								else:
									pass