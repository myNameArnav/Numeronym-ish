def numbersIPA(json: dict) -> list[str]:
    ipaNumbers = [
        json["zero"][0:8],
        json["one"],
        json["two"],
        json["three"],
        json["four"],
        json["five"],
        json["six"],
        json["seven"],
        json["eight"],
        json["nine"],
        json["ten"],
    ]
    result = cleanIPA(ipaNumbers)

    return result


def transformSentence(numbersIPA: list, ipaSentence: str) -> dict[str, str]:
    import re

    replaceDict = {}

    for counter, i in enumerate(numbersIPA):
        for word in ipaSentence:
            search = re.search(f"({i})", word)

            if search != None:
                search = search.span()
                replaced = word[: search[0]] + str(counter) + word[search[1] :]
                replaceDict[word] = replaced

    return replaceDict


def changeToIPA(ipaJSON: dict, sentence: str) -> list[str]:
    splitSentence = sentence.split()
    # print(splitSentence)
    ipaSentence = []
    for word in splitSentence:
        try:
            ipaWord = ipaJSON[word]
            if ", " in ipaWord:
                ipaWord = ipaWord.split(", ")[0]
            ipaSentence.append(ipaWord)
        except:
            ipaSentence.append(word)

    cleanIPASentence = cleanIPA(ipaSentence)

    return cleanIPASentence


def cleanIPA(ipaSentence: list[str]) -> list[str]:
    import re

    ipaCleanSentence = []

    for word in ipaSentence:
        try:
            span = re.search(pattern="(\/ˈ)", string=word).span()
            cleanWord = word[span[1] : -1]
            ipaCleanSentence.append(cleanWord)
        except:
            ipaCleanSentence.append(word)

    return ipaCleanSentence


def ipaToWords(sentence: str, ipaSentence: str, transformedSentence: str) -> list[str]:
    finalSentence = []

    # TODO: Implement areEqual()
    inputSentence = sentence.split()
    if len(inputSentence) == len(ipaSentence) == len(transformedSentence):
        for i in range(len(inputSentence)):
            if ipaSentence[i] == transformedSentence[i]:
                finalSentence.append(inputSentence[i])
            else:
                finalSentence.append(transformedSentence[i])
    else:
        print("Error")

    return finalSentence
