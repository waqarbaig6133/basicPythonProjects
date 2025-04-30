def bitgenerator(n):
  i=0
  powers=[]
  while 2**i <=n:
    powers.append(2**i)
    i+=1
  bits=[]
  for x in powers[::-1]:
    if n-x >= 0:
      bits.append(1)
      n-=x
    else:
      bits.append(0)
  return ''.join([str(x) for x in bits[::-1]])
