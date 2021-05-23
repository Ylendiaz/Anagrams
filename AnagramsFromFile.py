from collections import defaultdict
from itertools import combinations
from collections import defaultdict
from itertools import islice


counter = 0
count = 1

#abre archivo
def fileReader(fileName):
    with open(fileName) as file:
        lines = (x[:-1].lower() for x in file.readlines())
        words = list(islice(lines, 338882))
    return words
    
#sortea
def key(w):
  return "".join(sorted(w))

#crea tupla con combinaciones
def getAnagram(d):
    d = defaultdict(list)
    for w in wordList:
        d[key(w)].append(w)

    anagrams = [tuple(r) for v in d.values() for r in combinations(v, 2 )]
    return anagrams

def isNotDuplicated(line):
    return line[0] != line[1]

#imprime
def printLines(anagrams):
    printList ="\nLas palabras anagramas en el documento son:\n"

    for line in anagrams:
        if(isNotDuplicated(line)):
            printList += str(line) + "\n"       
    printList += ""
    # return printList 
    
    file = open("anagramsListResult.txt","w") 
    file.write(printList)
    file.close     


# def createFile(printList):
#     file = open("anagramsListResult.txt","w") 
#     file.write(printList)
#     file.close


file = "words.txt"
wordList = fileReader(file)
anagramList = getAnagram(wordList)
# print(printLines(anagramList))
printLines(anagramList)
# createFile(printList)