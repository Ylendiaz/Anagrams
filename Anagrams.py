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

#mete diccionario
def dictAppender(wordList):
    d = defaultdict(list)
    for w in wordList:
        d[key(w)].append(w)
    return d

#crea tupla con combinaciones
def getAnagram(d):
    anagrams = [tuple(r) for v in d.values() for r in combinations(v, 2 )]
    return anagrams

#imprime
def printLines(anagrams):
    printList ="\nLas palabras anagramas en el documento son:\n"

    for line in anagrams:
        if(line[0] != line[1]):
            printList += str(line) + "\n"       
    printList += ""
    return printList      


file = "words.txt"
wordList = fileReader(file)
dictList = dictAppender(wordList)
anagramList = getAnagram(dictList)
print(printLines(anagramList))
