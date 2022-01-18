#поменяйте местами значения двух переменных
var1 = input()
var2 = input()
var3 = var1
var1 = var2
var2 = var3
print(var1, var2)
#дано трехзначное число. Найдите произведение их цифр
num1 = int(input())
num2 = num1 // 100
num3 = num1 // 10 % 10
num4 = num1 % 100 % 10
result = num2 * num3 * num4
print(result)
#даны два трехзначных числа. Найдите шестизначное число, образованное из двух данных чисел путем дописывания второго числа к первому справа
num1 = str(input())
num2 = str(input())
print(num1 + num2)
#дано трехзначное число. Замените среднюю цифру на ноль
num1 = str(input())
spisok = list(num1)
spisok[1] = 0
print(spisok[0], spisok[1], spisok[2], sep="")
#дано трехзначное число. Выведите на экран новое число, полученное из исходного путем перестановки цифр в обратном порядке
num1 = input()
spisok = list(num1)
print(spisok[2], spisok[1], spisok[0], sep="")