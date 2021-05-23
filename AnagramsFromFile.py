
from collections import Counter

def word_hash(word):
  return frozenset(Counter(word).items())

def read_word_file():
  with open('words.txt') as f:
    words = f.read().splitlines()
  return words

def isNotDuplicated(line):
    return line[0] != line[1]

def getAnagrams(d):
  words = read_word_file()

  d = {}

  for word in words:
    k = word_hash(word)
    if k in d:
      d[k].append(word)
    else:
      d[k] = [word]

  # Prints the filtered results to only words with anagrams
  printList = ([x for x in d.values() if len(x) > 1])

  return printList


def printLines(printList):
  print("\nLas palabras anagramas en el documento son:\n")
  
  file = open("anagramsListResult.txt","w") 
  for elements in printList:
    file.write("%s\n" % elements)
  file.close   




if __name__ == "__main__":
  
  # reads file into memory
  
  file = "words.txt"
  wordList = read_word_file()
  anagramList = getAnagrams(wordList)
  printLines = (anagramList)

  
