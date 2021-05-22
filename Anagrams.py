from collections import defaultdict
from itertools import combinations
from collections import defaultdict
from itertools import islice

counter = 0
with open("words.txt") as file:
    lines = (x[:-1].lower() for x in file.readlines())
    words = list(islice(lines, 3000))
    
def key(w):
  return "".join(sorted(w))

d = defaultdict(list)
for w in words:
    d[key(w)].append(w)

anagrams = [tuple(r) for v in d.values() for r in combinations(v, 2)]


print ("\nLas palabras anagramas en el documento son:\n")

for words in anagrams:
    for i in words:
        print(list(dict.fromkeys(anagrams[counter])))
        counter += 1 

print("")      
