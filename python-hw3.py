#Написать калькулятор для вычисления дискриминанта. На вход подаются коэффициенты квадратного уравнения, выход - значение дискриминанта.
a = float(input())
b = float(input())
c = float(input())
D = b ** 2 - 4 * a * c
print(D)

#По данному целому числу N распечатайте все квадраты натуральных чисел, не превосходящие N, в порядке возрастания
N = int(input())
num_1 = 0
i = 1
num_2 = []
while num_1 <= N:
    num_1 = i**2
    i += 1
    num_2.append(a)
for i in range(len(num_2)):
    if num_2[i] <= N:
        print(num_2[i])

#Дано целое число, не меньшее 2. Выведите его наименьший натуральный делитель, отличный от 1.
num_1 = int(input())

for i in range(1,num_1 + 1):
    if num_1 % i == 0 and i != 1:
        print(i)
        break

#Последовательность Фибоначчи определяется так: f_0 = 0,  f_1 = 1,  f_n = f_{n−1} + f_{n−2} По данному числу n определите n-е число Фибоначчи f_n.
f_1 = 0
f_2 = 1
n = int(input())
for i in range(n):
    f_sum = f_1 + f_2
    f_1 = f_2
    f_2 = f_sum
print(f_1)

#Выведите все элементы списка с четными индексами (то есть A[0], A[2], A[4], ...)
A = [0, 1, 2, 3, 4 ,5 ,6 ,7 ,8, 9, 10]
for i in range(len(A)):
    if i % 2 == 0:
        print(A[i])

#Bыведите все четные элементы списка. При этом используйте цикл for, перебирающий элементы списка, а не их индексы
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in numbers:
    if int(i) % 2 == 0:
       print(i)

#Дан список чисел. Если в нем есть два соседних элемента одного знака, выведите эти числа. Если соседних элементов одного знака нет — не выводите ничего. Если таких пар соседей несколько — выведите первую пару.
A = [1, -2, -3, 4, 5, -6, -7]

b = -1
c = -1
d = -1
e = -1

for i in range(len(A)):
    if A[i] < 0:
        c = 1
        b = 0
    else:
        c = 0
        b = 1
    if (c == 1 and e == 1) or (b == 1 and d == 1):
        print(A[i-1], A[i])
        break
    else:
        e = c
        d = b
        c = -1
        b = -1

#Последовательность состоит из натуральных чисел и завершается числом 0. Определите, сколько элементов этой последовательности больше предыдущего элемента.
a = 0
b = 0
c = -767
while c != 0:
    c = int(input())
    if c > a:
        b += 1
    a = c
print(b - 1)

#Дан список чисел. Определите, сколько в этом списке элементов, которые больше двух своих соседей, и выведите количество таких элементов. Крайние элементы списка никогда не учитываются, поскольку у них недостаточно соседей.
numbers=[2, 5, 7, 3, 8, 1, 4, 7, 2, 0]
a=0
for i in range (3,len(numbers)-1):
    if numbers[i-2]<numbers[i-1] and numbers[i-1]>numbers[i]:
        a+=1
print(a)

#Петя перешёл в другую школу. На уроке физкультуры ему понадобилось определить своё место в строю. Помогите ему это сделать. Программа получает на вход невозрастающую последовательность натуральных чисел, означающих рост каждого человека в строю. После этого вводится число X – рост Пети. Все числа во входных данных натуральные и не превышают 200. Выведите номер, под которым Петя должен встать в строй. Если в строю есть люди с одинаковым ростом, таким же, как у Пети, то он должен встать после них.
height = [int(i) for i in input().split()]
x = int(input())
position = 0
while position < len(height) and height[position] >= x:
    position += 1
print(position + 1)

#Дан список, упорядоченный по неубыванию элементов в нем. Определите, сколько в нем различных элементов.
a = [int(i) for i in input().split()]
b = 1
for i in range(0, len(a) - 1):
    if a[i] != a[i + 1]:
        b += 1
print(b)

#Дан список, упорядоченный по неубыванию элементов в нем. Определите, сколько в нем различных элементов
list = [int(i) for i in input().split()]
number = 1
for i in range(0, len(a) - 1):
    if list[i] != list[i + 1]:
        number += 1
print(number)

# Дан список чисел. Выведите значение наибольшего элемента в списке, а затем индекс этого элемента в списке. Если наибольших элементов несколько, выведите индекс первого из них.
ya_uzhe_ne_znayu_kak_nazvat_spisok_nadoeli_defoltnye_nazvaniya = [int(i) for i in input().split()]
i_love_ayap = 0
for i in range(1, len(ya_uzhe_ne_znayu_kak_nazvat_spisok_nadoeli_defoltnye_nazvaniya)):
    if ya_uzhe_ne_znayu_kak_nazvat_spisok_nadoeli_defoltnye_nazvaniya[i] > ya_uzhe_ne_znayu_kak_nazvat_spisok_nadoeli_defoltnye_nazvaniya[m]:
        i_love_ayap = i
print(ya_uzhe_ne_znayu_kak_nazvat_spisok_nadoeli_defoltnye_nazvaniya[i_love_ayap], i_love_ayap)

#Последовательность состоит из натуральных чисел и завершается числом 0. Определите, сколько элементов этой последовательности равны ее наибольшему элементу.
#я сдался, пусть и дальше будут дефолтные названия списков и переменных.
a = 0
b = 0
c = -1
while c != 0:
    c = int(input())
    if c > a:
        a, b = c, 1
    elif c == a:
        b += 1
print(b)

# Дана последовательность натуральных чисел, завершающаяся числом 0. Определите, какое наибольшее число подряд идущих элементов этой последовательности равны друг другу.
b = -1
c = 0
m = 0
a = int(input())
while a != 0:
    if b == a:
        c += 1
    else:
        b = a
        m = max(m, c)
        c = 1
    a = int(input())
m = max(m, c)
print(m)

#Даны два списка с числами, получить третий путем поэлементного сложения первых двух
#А, может, вернуться к прикольным названиям списков? Хм..
i_love_mai = [1, 2, 3, 4, 5]
hochu_avtomat = [1, 2, 3, 4, 10, 12, 15]
no_avtomatov_net = list()
a = len(i_love_mai)
b = len(hochu_avtomat)
max1 = max(len(i_love_mai), len(hochu_avtomat))
min1 = min(len(i_love_mai), len(hochu_avtomat))
for k in range(min1, max1):
    x = 0
    if max1 == a:
        hochu_avtomat.append(x)
    else:
        i_love_mai.append(x)
for i in range(max1):
    s = i_love_mai[i] + hochu_avtomat[i]
    no_avtomatov_net.append(s)
print(no_avtomatov_net)

# Даные два вектора (списка), вычислить скалярное произведение
ne_ozhidal_tut_matan = [2, 3, 6]
on_vezde_menya_presledyuet = [3, 4, 5]
print(sum(p * q for p, q in zip(ne_ozhidal_tut_matan, on_vezde_menya_presledyuet)))


