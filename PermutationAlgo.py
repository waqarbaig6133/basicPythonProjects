collection = ['ABC']
def perm(x):
    thing = list(x)
    i = 0
    for letter in enumerate(thing):
        for numb in range(len(x)-1):
            copy = thing.copy()
            if numb != letter[0]:
                copy[numb],copy[letter[0]] = copy[letter[0]],copy[numb]
                if ''.join(copy) not in collection:
                    collection.append(''.join(copy))
            
        i+=1
        if i == len(thing):
            i = 0
perm('ABC')
for x in collection:
    if x[::-1] not in collection:
        collection.append(x[::-1])
print(collection)
