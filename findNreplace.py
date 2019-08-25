sentence = 'hate in the nation'
sentenceSplit = ['hate', 'in', 'the', 'nation']
pspelling = ['ðɛː', 'ɪz', 'ə', 'lɒt', 'ɒv', 'heɪt', 'ɪn', 'ðə', 'ˈneɪʃ(ə)n', 'wɪð', 'mɔː', 'heɪt']
numPspelling = ['wʌn', 'tuː', 'θriː', 'fɔː', 'fʌɪv', 'sɪks', 'ˈsɛv(ə)n', 'eɪt', 'nʌɪn', 'ˈzɪərəʊ']
#numspelling = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'zero']
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
sentence1 = 'hate in the nation'
#check if pspelling has any of numPspelling in them

combined = {'1': 'wʌn', '2': 'tuː', '3': 'θriː', '4': 'fɔː', '5': 'fʌɪv', '6': 'sɪks', '7': 'ˈsɛv(ə)n', '8': 'eɪt', '9': 'nʌɪn', '0': 'ˈzɪərəʊ'}
print(sentenceSplit)

for j in range(0, len(numPspelling)):
    for i in range(0, len(pspelling)):
        subfinder = pspelling[i].find(numPspelling[j])
        if subfinder != -1:
            print()
        else:
            print()
        print(subfinder,pspelling[i],numPspelling[j])
        i = i + 1
    j = j + 1