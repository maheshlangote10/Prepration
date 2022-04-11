import math

def get_perfect_sqrt(n):
    print("n , ceil =",n,  math.ceil(math.sqrt(n)))
    print("n ,floor",n, math.floor(math.sqrt(n)))
    if math.ceil(math.sqrt(n)) == math.floor(math.sqrt(n)):
        return n
    else:
        return None

for i in range(9,25+1):
    if get_perfect_sqrt(i):
        print(i)