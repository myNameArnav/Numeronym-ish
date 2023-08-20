from util import readJSON, findAndReplace, arrayAsString
from ipa import numbersIPA, changeToIPA, transformSentence, ipaToWords
from downloadJSON import downloadIPAJson
from os.path import exists


def main():
    if not exists("IPA.json"):
        downloadIPAJson()

    ipaJSON = readJSON("IPA.json")
    ipaNumbers = numbersIPA(ipaJSON)
    sentence = input("Enter a sentence: ")
    ipaSentence = changeToIPA(ipaJSON, sentence)
    transformedSentence = transformSentence(ipaNumbers, ipaSentence, sentence)
    findReplace = findAndReplace(ipaSentence, transformedSentence)
    finalSentence = ipaToWords(sentence, ipaSentence, findReplace)
    arrayAsString(finalSentence)


if __name__ == "__main__":
    main()
