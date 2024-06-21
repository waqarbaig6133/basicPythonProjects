    primes = []
    options = list(range(2,10))
    i = 0
    for x in range(2,x+1):# for all numbers in the list [2,3,4....x+1]
        for y in options: # for all mumbers in the list[2,3,4,5,6,7,8,9]
            if x != y:
                if x%y == 0: # if x is divisible by y (no remainder)
                    i+=1
                    break
        if i == 0:
            primes.append(x)
            i=0
        i = 0
  print(primes)
