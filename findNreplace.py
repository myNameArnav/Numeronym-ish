sentenceSplit = ['hate', 'in', 'the', 'nation']
pspelling = ['heɪt', 'tə', 'ðə', 'ˈneɪʃ(ə)n']
numPspelling = ['wʌn', 'tuː', 'θriː', 'fɔː', 'fʌɪv', 'sɪks', 'ˈsɛv(ə)n', 'eɪt', 'nʌɪn', 'ˈzɪərəʊ']
numspelling = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'zero']
#check if pspelling has any of numPspelling in them
combined = dict(zip(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'zero'], ['wʌn', 'tuː', 'θriː', 'fɔː', 'fʌɪv', 'sɪks', 'ˈsɛv(ə)n', 'eɪt', 'nʌɪn', 'ˈzɪərəʊ']))
s = " "
s = s.join(pspelling)
for i in range(0, len(numPspelling)):
    find = s.find(numPspelling[i])
    i = i + 1
print(combined)