import requests
from bs4 import BeautifulSoup

def sentence():
    inputSentence = input("Write a sentence: ")
    sentenceSplit = inputSentence.split()
    lenSentence = len(sentenceSplit)
    print(sentenceSplit)
    
sentence()