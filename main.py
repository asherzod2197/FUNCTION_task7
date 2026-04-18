# 11
def fibonacci(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# 12
def raqamlar_yigindisi(n):
    return sum(int(d) for d in str(abs(n)))

# 13
def takroriy_ochir(lst):
    return list(set(lst))

# 14
def ikkilik(n):
    return bin(n)[2:]

# 15
def alifbo_tartib(matn):
    return sorted(matn.split())

# 16
def max_min(lst):
    return max(lst), min(lst)

# 17
def saralash(lst):
    return sorted(lst)

# 18
def soz_uzunliklari(matn):
    return {s: len(s) for s in matn.split()}

# 19
def mukammal_son(n):
    return n == sum(i for i in range(1, n) if n % i == 0)

# 20
from math import gcd
def ekub_ekuk(a, b):
    return gcd(a, b), a * b // gcd(a, b)

print(fibonacci(7))
print(raqamlar_yigindisi(1234))
print(takroriy_ochir([1, 2, 2, 3, 3]))
print(ikkilik(10))
print(alifbo_tartib("banana olma anor"))
print(max_min([3, 1, 7, 2]))
print(saralash([5, 2, 8, 1]))
print(soz_uzunliklari("Men Python o'rganaman"))
print(mukammal_son(6))
print(ekub_ekuk(12, 8))
