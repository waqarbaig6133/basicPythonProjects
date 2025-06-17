import nltk
nltk.download('words')

from nltk.corpus import words
from random import choice

a=[x.upper() for x in words.words() if len(x) == 5]
c = choice(a)

i = 0
while i<=4: 
  word = input('Enter word: ')
  b = word.upper()
  if b not in a:
    print('Not a word')
  elif b != c.upper():
    for x in enumerate(b):
      if x[1] in c:
        if x[1] == c[x[0]]:
          print(f"{x[1]} is there")
        else:
          print(f"{x[1]} is in the wrong place")
      else:
        print(f"{x[1]} is not there")
    i+=1
  else:
    print('You win')
    break
if i== 5:
  print(f"the word was {c}")
  
          
