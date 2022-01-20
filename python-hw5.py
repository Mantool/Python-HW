#Написать функцию, которая вычисляет среднее арифметическое элементов массива, переданного ей в качестве аргумента.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = len(numbers)
def result():
    c = 0
    for i in range (a):
        c += numbers[i]
    s = c / a
    return s
print(result())
#Написать две функции, которые будут переводить из десятичной СС в двоичную и обратно.
def binary(n):
    s = int(n)
    b = ''
    while s > 0:
        b = str(s % 2) + b
        s = s // 2
    return b
def binary_2(n):
    m = 1
    out = 0
    for i in n[::-1]:
        if i == '1': out += m
        m <<=1
    return out
n = input()
print(binary(n), binary_2(n))
#Пользователь делает вклад в размере a рублей сроком на years лет под 10% годовых (каждый год размер его вклада увеличивается на 10%. Эти деньги прибавляются к сумме вклада, и на них в следующем году тоже будут проценты).
#Написать функцию bank, принимающая аргументы a и years, и возвращающую сумму, которая будет на счету пользователя.
def bank(a, years):
    while years > 0:
        a = float(a * 0.1) + a
        years -= 1
    return a
a = float(input())
years = int(input())
print(bank(a, years))
#Даны четыре действительных числа: x1, y1, x2, y2. Напишите функцию distance(x1, y1, x2, y2), вычисляющая расстояние между точкой (x1,y1) и (x2,y2). Считайте четыре действительных числа и выведите результат работы этой функции.
def distance(x1, x2, y1, y2):
    length = ((x2 - x1) ** 2 + (y2-y1) ** 2) ** 0.5
    return length
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
print(distance(x1, x2, y1, y2))
#Дано действительное положительное число a и целоe число n.
#Вычислите a^n. Решение оформите в виде функции power(a, n).
#Стандартной функцией возведения в степень пользоваться нельзя.
#Учтитье, что n может быть отрицательным.
def power(a, n):
    if n > 0:
        s = a
        for i in range(n - 1):
            s *= a
        return s
    elif n < 0:
        s = 1 / a
        for i in range(abs(n) - 1):
            s *= (1 / a)
        return s
    else:
        return 1
a = float(input())
n = int(input())
print(power(a, n))
#Написать функцию is_prime, принимающую 1 аргумент — число от 0 до 1000, и возвращающую True, если оно простое, и False - иначе
def is_prime(a):
    b = 0
    flag = False
    for i in range(1, a + 1):
        if a % i == 0:
            b += 1
    if b == 2:
        flag = True
    return flag
a = int(input())
print(is_prime(a))