import requests
from bs4 import BeautifulSoup

sentenceSplit = ['hate', 'in', 'the', 'nation']
firstelement = str(sentenceSplit[0])
lastelement = str(sentenceSplit[-1])
"""for i in range(firstelement, lastelement):i = i + 1"""
url = "https://www.lexico.com/en/definition/" + "one" + "/"
print(url)
r = requests.get(url)
html_content = r.text
soup = BeautifulSoup(html_content, "html.parser")
line = soup.find(class_ = "phoneticspelling").text
spelling = line.replace("/", "")
print(spelling)
