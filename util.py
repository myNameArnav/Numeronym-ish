import json


def saveFile(
    content: str | bytes | list | dict,
    fileName: str,
    fileExtension: str = ".txt",
    mode: str = "w",
    encoding: str = "utf-8",
):
    stuff = ""
    if type(content) == list or type(content) == dict or fileExtension == ".json":
        stuff = json.dumps(content)
        fileExtension = ".json"

    if type(content) == bytes:
        mode = "wb+"

    if fileName == "idc":
        import uuid

        fileName = str(uuid.uuid4()) + fileExtension

    with open(fileName, mode, encoding=encoding) as f:
        if stuff == "":
            stuff = content
        f.write(stuff)


def readJSON(fileName: str):
    with open(fileName, "r", encoding="utf-8") as f:
        JSON = json.loads(f.read())

    return JSON


# TODO
def areEqual(*args) -> tuple[bool, int]:
    for elements in args:
        pass


def findAndReplace(ipaSentence: str, replaceDict: dict[str, str]):
    result = []

    for ipaWord in ipaSentence:
        try:
            result.append(replaceDict[ipaWord])
        except KeyError:
            result.append(ipaWord)

    return result


def arrayAsString(array: list):
    print(" ".join(x for x in array))
