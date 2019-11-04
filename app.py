import Numeronym.webscraper
import Numeronym.findNreplace2

sentenceSplit = ''
pspelling = []

inputSentence = input("Write a sentence: ")

def sentence(inputSentence):
	sentenceSplit = inputSentence.split()
	print(sentenceSplit)

sentence(inputSentence)
phoneticspelling(sentenceSplit)