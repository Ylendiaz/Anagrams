
from collections import Counter
import urllib.request


def word_hash(word):
  return frozenset(Counter(word).items())

def read_word_file():
  with open('words.txt') as f:
    words = f.read().splitlines()
  return words


if __name__ == "__main__":
  
  # reads file into memory
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
  file = open("anagramsListResult.txt","w") 
  for elements in printList:
    file.write("%s\n" % elements)
  file.close   

  file = "words.txt"