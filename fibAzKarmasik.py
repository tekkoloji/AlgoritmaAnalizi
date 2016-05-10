hafiza = {}    
def fib(n):
    if n not in hafiza.keys():
        hafiza[n] = bul(n)
    return hafiza[n]

def bul(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)

print fib(6)
