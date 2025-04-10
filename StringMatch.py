def thing(s1, s2):
    s = list(s1)
    thing = []
    for x in enumerate(s):
        t = s.copy()
        t.pop(x[0])
        if ''.join(t) == s2:
            thing.append(x[0])
    return thing
    
    
    
s1 = 'waqaar'
s2 = 'waqar'
result = thing(s1, s2)
for x in result:
    print(x) #Generate the indexes where s1 and s2 can be the same
