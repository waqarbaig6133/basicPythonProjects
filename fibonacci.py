#fibonacci sequence
def fibonacci(x):
        trivial = {
            1: [1],
            2: [1,1]
        }
        if x < 3:
            print(trivial[x])
        else:
            lis = [1,1]
            while len(lis) < x:
                sums = lis[len(lis)-1] + lis[len(lis)-2]
                lis.append(sums)
                
        return lis
