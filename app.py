# coding=utf-8

from webscraper import *

sentenceSplit = ""
pspelling = []

inputSentence = input("Write a sentence: ")

def sentence(inputSentence):
	sentenceSplit = inputSentence.split()
	return sentenceSplit

sentence(inputSentence)
print(sentenceSplit)
phoneticspelling(sentenceSplit)
print(pspelling)

