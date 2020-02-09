#Задачи на циклы и оператор условия------
#----------------------------------------

"""
Задача 1
Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
"""
print("Задача 1")
for i in range(1,6):
  print(i,"0" * i)

Задача 2
Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.

print("Задача 2")
y = 0

for m in range(10):
    x = input('Введите число')
    x = int(x)
    if x == 5: y = y + 1
    continue
print("Число 5 введено " , y," раз(а)")


"""
Задача 3
Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
"""
print("Задача 3")
sum = 0
for i in range(1,101):
    sum+=i
print(sum)
print('')
"""
Задача 4
Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
"""
print("Задача 4")

i=2
s=1
while i<=10:
    s=i*s
    i=i+1
print ("Произведение чисел от 1 до 10 = ", s)


"""
Задача 5
Вывести цифры числа на каждой строчке.
"""

print("Задача 5")
integer_number = 2129
print(integer_number%10,integer_number//10)
while integer_number>0:
    print(integer_number%10)
    integer_number = integer_number//10
print('')
""""
Задача 6
Найти сумму цифр числа.
"""
print("Задача 6")

N = int(input("Введите число="))
sum = 0
while N > 0:
    d = N%10
    N = N // 10
    sum += d
print("Сумма всех цифр этого числа =",sum)

"""
Задача 7
Найти произведение цифр числа.
"""
print("Задача 7")

n = int(input("Введите число="))
u = 1
while n > 0:
    if n % 10 != 0:
        u = u * (n % 10)
        n = n // 10

print("Произведение значащих цифр:", u)

""""
Задача 8
Дать ответ на вопрос: есть ли среди цифр числа 5?
"""
print("Задача 8")
integer_number = 213413
while integer_number>0:
    if integer_number%10 == 5:
        print('Yes')
        break
    integer_number = integer_number//10
else: print('No')
"""
Задача 9
Найти максимальную цифру в числе
"""
print("Задача 9")
integer_number = 123456
q = 0
while integer_number>0:
    if integer_number%10 >= q:
        q = integer_number%10
    integer_number = integer_number//10
print('максимальное число:', q)

"""
Задача 10
Найти количество цифр 5 в числе
"""
print('Задача 10')
integer_number = 4523346
p = 0
while integer_number>0:
    if integer_number%10 == 5:
        p += 1
    integer_number = integer_number//10
print('количество цифр 5 :', p)
"""