import requests
from bs4 import BeautifulSoup

sentenceSplit = ['hate', 'in', 'the', 'nation']
elements = len(sentenceSplit)
pspelling = []

for i in range(0, elements):
    word = str(sentenceSplit[i])
    url = "https://www.lexico.com/en/definition/" + word + "/"
    print(url)
    r = requests.get(url)
    html_content = r.text
    soup = BeautifulSoup(html_content, "html.parser")
    line = soup.find(class_="phoneticspelling").text
    spelling = line.replace("/", "")
    pspelling.append(spelling)
    i = i + 1

print(pspelling)
