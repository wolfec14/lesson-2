# проверка на простое число
def IsPrime(n):
    d = 2
    while n % d != 0 and d != n + 1:
        d += 1
        if d == n and n % d == 0:
            print("число является натуральным")


# делители
def delimeter(n):
    print("Делители:", end=" ")
    for i in range(n - 1, 1, -1):
        if (n % i == 0):
            print(i, end=" ")


# максимальный делитель
def maxd(n):
    max_divider = 1
    for i in range(n - 1, 1, -1):
        if (n % i == 0):
            if (max_divider <= i):
                max_divider = i
    print("Максимальный делитель кроме числа", n, " равен:", max_divider)


#каноническое разложение числа

def Factor(n):
    Ans = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            Ans.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        Ans.append(n)
    print('каноническое разложение числа:', Ans)
