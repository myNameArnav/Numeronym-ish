# coding=utf-8
import Numeronym.webscraper
import Numeronym.app
sentence = "hate in the nation"
sentenceSplit = ['hate', 'in', 'the', 'nation']

finalString = sentence
def findNreplace(pspelling):
    num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    for x in range(len(numPspelling)):
        if __name__ == '__main__':
            txt = " ".join(pspelling)
            pat = numPspelling[x]
            M = len(pat)
            N = len(txt)
            # A loop to slide pat[] one by one */
            for i in range(N - M + 1):
                j = 0

                # For current index i, check
                # for pattern match */
                while(j < M):
                    if (txt[i + j] != pat[j]):
                        break
                    j += 1

                if (j == M):
                    #print("Pattern found at index ", i, "of number", x+1)
                    print(finalString[:i] + str(num[x]) + finalString[i+len(numPspelling[x]):])