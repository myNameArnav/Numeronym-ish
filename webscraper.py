import requests
from bs4 import BeautifulSoup

sentenceSplit = ['hate', 'in', 'the', 'nation']
elements = len(sentenceSplit)
pspelling = []

for i in range(0, elements):
	word = str(sentenceSplit[i])
	url = "https://www.lexico.com/en/definition/" + word + "/"
	#print(url)
	r = requests.get(url)
	html_content = r.text
	soup = BeautifulSoup(html_content, "html.parser")
	line = soup.find(class_="phoneticspelling").text
	spelling = line.replace("/", "")
	pspelling.append(spelling)
	i = i + 1
	print(str(i) + "th word is " + str(sentenceSplit[i]))
	print(pspelling)


#['ə', 'əˈbɪlɪti', 'ˈeɪb(ə)l', 'əˈbaʊt', 'əˈbʌv', 'əkˈsɛpt', 'əˈkɔːdɪŋ', 'əˈkaʊnt', 'əˈkrɒs', 'akt', 'ˈakʃ(ə)n', 'akˈtɪvɪti', 'ˈaktʃəli', 'ad', 'əˈdrɛs', 'ədmɪnɪˈstreɪʃ(ə)n', 'ədˈmɪt', 'ˈadʌlt', 'əˈfɛkt', 'ˈɑːftə', 'əˈɡɛn', 'əˈɡɛnst', 'eɪdʒ', 'ˈeɪdʒ(ə)nsi', 'ˈeɪdʒ(ə)nt', 'əˈɡəʊ', 'əˈɡriː', 'əˈɡriːm(ə)nt', 'əˈhɛd', 'ɛː', 'ɔːl', 'əˈlaʊ', 'ˈɔːlməʊst', 'əˈləʊn', 'əˈlɒŋ', 'ɔːlˈrɛdi', 'ˈɔːlsəʊ', 'ɔːlˈðəʊ', 'ˈɔːlweɪz', 'əˈmʌŋ', 'əˈmaʊnt', 'əˈnalɪsɪs', 'ənd', 'ˈanɪm(ə)l', 'əˈnʌðə', 'ˈɑːnsə', 'ˈɛni', 'ˈɛnɪwʌn', 'ˈɛnɪθɪŋ', 'əˈpɪə', 'əˈplʌɪ', 'əˈprəʊtʃ', 'ˈɛːrɪə', 'ˈɑːɡjuː', 'ɑːm', 'əˈraʊnd', 'əˈrʌɪv', 'ɑːt', 'ˈɑːtɪk(ə)l', 'ˈɑːtɪst', 'az', 'ɑːsk', 'əˈsjuːm', 'at', 'əˈtak', 'əˈtɛnʃ(ə)n', 'əˈtəːni', 'ˈɔːdɪəns', 'ˈɔːθə', 'ɔːˈθɒrɪti', 'əˈveɪləb(ə)l', 'əˈvɔɪd', 'əˈweɪ', 'ˈbeɪbi', 'bak', 'bad', 'baɡ', 'bɔːl', 'baŋk', 'bɑː', 'beɪs', 'biː', 'biːt', 'ˈbjuːtɪfʊl', 'bɪˈkɒz', 'bɪˈkʌm', 'bɛd', 'bɪˈfɔː', 'bɪˈɡɪn', 'bəˈhāvyər', 'bɪˈhʌɪnd', 'bɪˈliːv', 'ˈbɛnɪfɪt', 'bɛst', 'ˈbɛtə', 'bɪˈtwiːn', 'bɪˈjɒnd', 'bɪɡ', 'bɪl', 'ˈbɪljən', 'bɪt', 'blak', 'blʌd', 'bluː', 'bɔːd', 'ˈbɒdi', 'bʊk', 'bɔːn', 'bəʊθ', 'bɒks', 'bɔɪ', 'breɪk', 'brɪŋ', 'ˈbrʌðə', 'ˈbʌdʒɪt', 'bɪld', 'ˈbɪldɪŋ', 'ˈbɪznəs', 'bʌt', 'bʌɪ', 'bʌɪ', 'kɔːl', 'ˈkam(ə)rə', 'kamˈpeɪn', 'kan', 'ˈkansə', 'ˈkandɪdeɪt', 'ˈkapɪt(ə)l', 'kɑː', 'kɑːd', 'kɛː', 'kəˈrɪə', 'ˈkari', 'keɪs', 'katʃ', 'kɔːz', 'sɛl', 'ˈsen(t)ər', 'ˈsɛntr(ə)l', 'ˈsɛntʃʊri', 'ˈsəːt(ə)n', 'ˈsəːt(ə)nli']