# coding=utf-8
import requests
from bs4 import BeautifulSoup

pspelling = []

def phoneticspelling(sentenceSplit):
    elements = len(sentenceSplit)
    for i in range(0, elements):
        word = str(sentenceSplit[i])
        url = "https://www.lexico.com/en/definition/" + word + "/"
        # print(url)
        r = requests.get(url)
        html_content = r.text
        soup = BeautifulSoup(html_content, "html.parser")
        line = soup.find(class_="phoneticspelling").text
        spelling = line.replace("/", "")
        pspelling.append(spelling)
        i = i + 1
        #print(str(i) + "th word is " + str(sentenceSplit[i]))
    return pspelling