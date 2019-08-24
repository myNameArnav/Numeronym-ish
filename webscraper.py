import requests
from bs4 import BeautifulSoup

sentenceSplit = ['hate', 'in', 'the', 'nation']
elements = int(len(sentenceSplit))
pspelling = []
for i in range(-1, elements-1):
    i = i + 1
    url = "https://www.lexico.com/en/definition/" + str(sentenceSplit[i]) + "/"
    print(url)
    r = requests.get(url)
    html_content = r.text
    soup = BeautifulSoup(html_content, "html.parser")
    line = soup.find(class_ = "phoneticspelling").text
    spelling = line.replace("/", "")
    pspelling.append(spelling)
print(pspelling)
