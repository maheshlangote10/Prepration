def fibo(limit):
    a,b = 0,1
    while a<limit:
        yield a
        a,b = b, a+b

f = fibo(6)
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
