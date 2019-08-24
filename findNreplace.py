sentenceSplit = ['hate', 'in', 'the', 'nation']
pspelling = ['heɪt', 'tə', 'ðə', 'ˈneɪʃ(ə)n']
numPspelling = ['wʌn', 'tuː', 'θriː', 'fɔː', 'fʌɪv', 'sɪks', 'ˈsɛv(ə)n', 'eɪt', 'nʌɪn', 'ˈzɪərəʊ']
numspelling = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'zero']
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

#check if pspelling has any of numPspelling in them

combined = {'one': 'wʌn', 'two': 'tuː', 'three': 'θriː', 'four': 'fɔː', 'five': 'fʌɪv', 'six': 'sɪks', 'seven': 'ˈsɛv(ə)n', 'eight': 'eɪt', 'nine': 'nʌɪn', 'zero': 'ˈzɪərəʊ'}
example = sentenceSplit[0]
print(example)

for i in range(len(example)):
    